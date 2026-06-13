import requests
from backend.core.config import settings

def get_stock_earnings(ticker: str):
    url = "https://stock-analysis.p.rapidapi.com/api/v1/resources/earnings-history"
    headers = {
        "x-rapidapi-key": settings.RAPID_API_KEY,
        "x-rapidapi-host": "stock-analysis.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params={"ticker": ticker})
    return response.json()