import requests
import json
import sys
from dotenv import load_dotenv
import os

from typing import Optional


def get_api_token() -> Optional[None]:
    url = "https://wmsapi.logiwa.com/token"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    body = {
        "grant_type": "password",
        "username": os.getenv("LOGIWA_USERNAME"),
        "password": os.getenv("LOGIWA_PASSWORD"),
    }

    res = requests.post(url, data=body, headers=headers)

    print(res.text)

    res_body = res.json()
    if res_body.get("error"):
        print(res_body.get("error"))
    else:
        return res.json()["access_token"]


def main():
    print(get_api_token())
    print("Hello from logiwa-shipments!")


if __name__ == "__main__":
    if not load_dotenv():
        print("failed to load dotenv")
        sys.exit(1)
    main()
