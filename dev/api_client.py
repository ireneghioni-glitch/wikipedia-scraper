import requests

class CountryLeadersAPI:
    def __init__(self):
        self.base_url = "https://country-leaders.onrender.com/"
        self.countries_endpoint = self.base_url + "countries"
        self.leaders_endpoint = self.base_url + "leaders"
        self.cookies_endpoint = self.base_url + "cookie"

        self.session = requests.Session()  #Creates a persistent session
        self.cookies = None

        self.refresh_cookie()      # Calls a method to initialize a cookie
    
    def refresh_cookie(self)-> None:

        '''This refreshes the session cookie when it is missing or has expired'''
        try:
           response = self.session.get(self.cookies_endpoint) # This will create the cookie
           response.raise_for_status()      #This will stop the program instantly if the API gives an error 
          
           cookie_value = response.json()["cookie"] # This will retreive the cookie value
           self.cookies = {"session": cookie_value}           # Stores the cookie

        except requests.exceptions.RequestException as e:
             print(f"[ERROR] Failed to refresh cookie: {e}")
             self.cookies = None


    def get_countries(self)->list[str]:

        '''Will return the list of  country codes'''
        try:
          response = self.session.get(self.countries_endpoint, cookies = self.cookies) #request with stored cookie

          if response.status_code !=200:
            self.refresh_cookie()
            response = self.session.get(self.countries_endpoint,cookies=self.cookies)  #if request fails-->refresh cookie/retry request

          response.raise_for_status() #This will stop the program instantly if the API gives an error
          return response.json() #return the list of countries
    
        except requests.exceptions.RequestException as e:
         print(f"[ERROR] Failed to fetch countries: {e}")
         return[]
        
    

    
    def get_leaders(self, country:str)->list[dict]:

        '''Will return the json file for the leaders for a selected country'''
        try:
         response = self.session.get(self.leaders_endpoint,cookies=self.cookies,params={"country":country})

         if response.status_code != 200:
            self.refresh_cookie()
            response = self.session.get(self.leaders_endpoint,cookies=self.cookies,params={"country":country})
         response.raise_for_status()
         return response.json()
    
        except requests.exceptions.RequestException as e:
         print(f"[ERROR] Failed to fetch leaders for {country}: {e}")
         return[]

