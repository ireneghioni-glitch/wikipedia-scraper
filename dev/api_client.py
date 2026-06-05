import requests

class CountryLeadersAPI:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com/"
        self.countries_endpoint = self.base_url + "countries"
        self.leaders_endpoint = self.base_url + "leaders"
        self.cookies_endpoint = self.base_url + "cookie"

        self.session = requests.Session()

        self.refresh_cookie()
    
    def refresh_cookie(self)-> None:

        '''This refreshes the session cookie when it is missing or has expired'''

        self.session.get(self.base_url + self.cookies_endpoint)  # This will create the cookie
        cookie_value = self.session.get(self.base_url + self.cookies_endpoint).json()["cookie"] # This will retreive the cookie value
        self.cookies = {"session": cookie_value}           # Stores the cookie

    def get_countries(self)->list[str]:

        '''Will return the list of  country codes'''
        response = self.session.get(self.base_url+self.countries_endpoint, cookies = self.cookies)

        if response.status_code !=200:
            self.refresh_cookie()
            response = self.session.get(self.base_url+self.countries_endpoint,cookies=self.cookies)

        response.raise_for_status() #This will stop the program instantly if the API gives an error
        return response.json()
    
    def get_leaders(self, country:str)->list[dict]:

        '''Will return the json file for the leaders for a selected country'''
        if response.status_code != 200:
            self.refresh_cookie()
            response = self.session.get(self.base_url+self.leaders_endpoint,cookies=self.cookies,params="country")
        response.raise_for_status
        return response.json()

