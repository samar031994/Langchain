import json
import os
from dotenv import load_dotenv
import requests
from pprint import PrettyPrinter 

load_dotenv()
pp = PrettyPrinter(indent=4)

def scrape_linkedin_profile(url, mock=False):
    """
    Scrape information from a LinkedIn profile."""
    if mock:
        response = requests.get(
            "https://raw.githubusercontent.com/samarmanjeshwar/LangChain/main/ice_breaker/mock_linkedin_profile.json"
        )
    else:
        linkedin_endpoint = url
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ.get("SCRAPIN_API_KEY"),
            "linkedInUrl": linkedin_endpoint,
        }
        response = requests.get(api_endpoint, params=params, timeout=10)
        data = response.json().get("person")
        data = {
            k: v
            for k, v in data.items()
            if v not in ([], "", None) and k not in ["certifications"]
        }
        return data

if __name__ == "__main__":
    scrape_linkedin_profile(
        url="https://www.linkedin.com/in/eden-marco/"
    )
