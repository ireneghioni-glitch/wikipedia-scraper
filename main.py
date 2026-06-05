import requests
from requests import Session
from bs4 import BeautifulSoup
from urllib.parse import unquote
import json
from src.api_client import CountryLeadersAPI
from src.leaders_scraper import WikipediaScraper

# the coordinator
OUTPUT_FILE = "leaders_data.json"
def main():
    """
    Manages all functions to return the dictionary of all country leaders 
    with scraped first paragraph in it.
    """
    # URLs will be implemented as API_client from Neha will be imported
    api = CountryLeadersAPI()
    scraper = WikipediaScraper(session=api.session)
    
    leaders_per_country ={}
    countries = api.get_countries()

    for country in countries:
        leaders = api.get_leaders(country)
        for leader in leaders:
             leader["first_paragraph"] = scraper.get_first_paragraph(leader["wikipedia_url"])
        leaders_per_country[country] = leaders

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(leaders_per_country, f, ensure_ascii=False, indent=2)
    print(f"Saved leaders to {OUTPUT_FILE}")






if __name__ == "__main__":
    print(main())