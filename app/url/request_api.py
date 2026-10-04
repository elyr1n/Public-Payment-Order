import httpx
import re

from app.settings.config import neccesary_data
from app.url.get_submit_url import get_submit_url

headers = {
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "referer": "https://funpay.com/orders/new",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36 Edg/154.0.0.0",
    "x-requested-with": "XMLHttpRequest",
}


async def request_funpay():
    cookies = {
        "golden_key": neccesary_data["golden_key"],
        "PHPSESSID": neccesary_data["phpsessid"],
    }

    data = {"csrf_token": neccesary_data["csrf"], **neccesary_data["data"]}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://funpay.com/orders/new", cookies=cookies, headers=headers, data=data
        )
        json = response.json()

        try:
            if json["error"] > 0:
                return json["msg"]
        except KeyError:
            return "походу твой аккаунт твой акк забанили лоооох"

        link = re.search(r"https://.*/receipt", json["form"]).group()
        payment_id = link.split("/")[3]

        return await get_submit_url(payment_id)
