import requests


def coingecko_status():
    response = requests.get("https://api.coingecko.com/api/v3/ping")
    return response.json()
