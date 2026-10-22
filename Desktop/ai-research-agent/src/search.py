import requests

def check_api(url: str) -> dict:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        return response.json()
    else: 
        raise ValueError("API request failed")










def search_web(query: str) -> list[dict]:
    pass