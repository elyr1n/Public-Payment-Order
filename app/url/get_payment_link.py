from playwright.async_api import async_playwright


async def get_payment_link(payment_id):
    payment_link = (
        "если ты видишь это сообщение: то произошла какая-то ошибка\n\n"
        "причины:\n"
        "1. счет не найден\n"
        "2. счет просрочен\n"
        "3. ссылка не успела подгрузиться\n\n"
        "в лучшем случае - попробовать 2-3 раза ещё раз, либо полностью менять ссылку"
    )
    catch = False

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        async def on_response(resp):
            nonlocal payment_link, catch

            if "/process" in resp.request.url and resp.request.method == "POST":
                catch = True

            if (
                catch
                and f"api/v2/pay-form/invoice/{payment_id}" in resp.url
                and not "/fingerprint" in resp.url
                and not "/process" in resp.url
            ):
                try:
                    json = await resp.json()
                    data = json["data"]
                    message = json["message"]

                    if len(data) != 0 and data["payment"] != None:
                        payment_link = data["payment"]["payment_data"]["payment_link"]
                    else:
                        payment_link = message
                except Exception as e:
                    payment_link = f"ошибка: {e}"

        page.on("response", on_response)

        await page.goto(f"https://payform.aurapay.tech/{payment_id}")
        await page.wait_for_timeout(25000)

        await browser.close()

        catch = False

        return payment_link
