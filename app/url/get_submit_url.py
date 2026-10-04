from playwright.async_api import async_playwright


async def get_submit_url(payment_id):
    submit_url = ""

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        async def on_response(resp):
            if f"/api/payments/{payment_id}" in resp.url:
                nonlocal submit_url

                try:
                    submit_url = (await resp.json())["confirmation"]["submit_url"]
                except KeyError:
                    submit_url = "submit_url не был найден((("

        page.on("response", on_response)

        await page.goto(f"https://payment.tome.ge/{payment_id}/receipt")
        await browser.close()

    return submit_url
