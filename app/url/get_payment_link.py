from playwright.async_api import async_playwright


async def get_payment_link(payment_id):
    payment_link = ""

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        async def on_response(resp):
            if (
                f"api/v2/pay-form/invoice/{payment_id}" in resp.url
                and not "/fingerprint" in resp.url
            ):
                nonlocal payment_link

                json = await resp.json()
                data = json["data"]
                message = json["message"]

                try:
                    if len(data) != 0:
                        payment_link = data["payment"]["payment_data"]["payment_link"]
                    else:
                        payment_link = message

                    if data["payment"] == None:
                        payment_link = "да блин не удалось отправить ссылку, попробуй ещё раз гандон"
                except TypeError as e:
                    if data["state"] == "expired":
                        payment_link = "прогорел ебать твой счёт"

        page.on("response", on_response)

        await page.goto(f"https://payform.aurapay.tech/{payment_id}")
        await page.wait_for_timeout(25000)

        await browser.close()

        return payment_link
