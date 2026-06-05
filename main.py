import requests
from requests import Session
from bs4 import BeautifulSoup
import re
from urllib.parse import unquote
import json

from api_client import CountryLeadersAPI
from leaders_scraper import WikipediaScraper

# the coordinator
def main():
    """
    Manages all functions to return the dictionary of all country leaders 
    with scraped first paragraph in it.
    """
    # URLs will be implemented as API_client from Neha will be imported
    api = CountryLeadersAPI()
    leaders


    with Session() as session:
        # here in the main() of main.py there will be 2 variables
        # outpout of API_client
        # which wiil be input of scraping part
        # now get_leaders does both
        leaders_per_country = get_leaders(session)
    
    save(leaders_per_country)

    return leaders_per_country


if __name__ == "__main__":
    print(main())