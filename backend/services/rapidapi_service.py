import requests
from backend.core.config import settings

def search_jobs(query: str):
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "x-rapidapi-key": settings.RAPID_API_KEY,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params={"query": query, "page": "1", "num_pages": "1"})
    return response.json()