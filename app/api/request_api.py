import httpx

headers = {
    "accept": "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36 Edg/154.0.0.0",
}


async def request_aurapay_api(invoice):
    async with httpx.AsyncClient() as client:
        api_response = await client.get(
            f"https://api.aurapay.tech/api/v2/pay-form/invoice/{invoice}",
            headers=headers,
        )
        json = api_response.json()
        data = json["data"]
        message = json["message"]

        try:
            if len(data) != 0:
                return data["payment"]["payment_data"]["payment_link"]
            else:
                return message
        except TypeError as e:
            if data["payment"] == None:
                return "долбаеб зайди на ссылку и чета поделай"

            if data["state"] == "expired":
                return "прогорел ебать твой счёт"

        return "какая-то хуйня непонятная если честно"
