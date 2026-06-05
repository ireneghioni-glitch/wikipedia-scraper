import requests


class WikipediaScraper:

    HEADERS = {"User-Agent":"Wikipedia Scraper Project (https://github.com/ireneghioni-glitch/wikipedia-scraper/tree/main)"}

    def __init__(self, session:Sesion):
        self.session = session

    def fetch_html(self, url:str):
        """
        Safely requests raw HTML text. 
        Must include robust exception handling to deal with 404s, 500s, or connection drops.
        """
    # def get_text(url:str, session:Session):
    # headers = {"User-Agent":"Wikipedia Scraper Project (https://github.com/ireneghioni-glitch/wikipedia-scraper/tree/main)"}
    # # r = requests.get(wiki_url, timeout=10)
    # r = session.get(url, headers=headers, timeout=10)
    # return r.text

        try:
            response = self.session.get(url, headers=WikipediaScraper.HEADERS, timeout=10)
            response.raise_for_status() # will give an int: 200 or 404 or 500
            return response.text
        except requests.exceptions.RequestException as e:
            print(f'Network error Error: {e}.')
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f'{url} Not Found.')
            elif e.response.status_code == 500:
                print("Internet Server Error.")
        except requests.exceptions.ConnectionError:
            print(f'Connection Error: Immpossible to reach {url}.')
        except requests.exceptions.Timeout:
            print("Session is expired.")
    
    def get_first_paragraph(self, html: str):
        """
        Parses raw HTML with BeautifulSoup, 
        finds the first true biographical narrative paragraph (<p>), 
        and returns it.
        """
    
    
    def clean_text(self, text: str):
        """
        A cleaning utility method to strip out 
        unwanted characters, whitespace, or Wikipedia citation brackets 
        (e.g., [1], [citation needed]).
        """
    
    def to_json_file(self, filepath: str):
        """
        Stores the data structure into a JSON file,
        return None.
        """













def get_first_paragraph(wikipedia_url, session:Session):
    """
    the function returns first cleaned paragraph of the url leader.
    this version of the function is optimized for whatever the url
    """
    print (wikipedia_url) # keep this for the rest of the notebook
    leader_last_name = unquote(wikipedia_url.split("_")[-1]) # makes a list out of strings in the url seperated on "_" char
    soup = BeautifulSoup(get_text(wikipedia_url, session), "html.parser")
    paragraphs = [tag.text for tag in soup.find_all("p")]
    for paragraph in paragraphs:
        if leader_last_name in paragraph[:50]:
            #sanitizing output with Regex
            pattern_1 = r"\[\d+\]" # "|" stands for OR in regex
            pattern_2 = r"\([^()]*\)"
            while re.search(pattern_2, paragraph):
                paragraph = re.sub(pattern_2, "", paragraph)
            cleaned_paragraph = re.sub(pattern_1, "", paragraph)
            other_patterns = [r"\s+", r"\s+,", r"\s+\.", r"[ⓘ·]"]
            for pattern in other_patterns:
                cleaned_paragraph = re.sub(pattern, " ", cleaned_paragraph)
            return cleaned_paragraph

def get_leaders(session):
    """
    New version of get_leaders() function.
    Now it receives session.
    It loops over each leader to extract the leader url then
    Executes get_first_paragraph() that has just been optimized then
    Adds to dict of leader the leader name (key) and first cleaned paragraph (value)
    untill dictionary is complete.
    Returns the leader dictionary.
    """
    # declaration of url variables
    root_url = "https://country-leaders.onrender.com"
    cookie_url = f'{root_url}/cookie'
    countries_url = f'{root_url}/countries'
    leaders_url = f'{root_url}/leaders'
    # getting the cookies
    cookies = session.get(cookie_url).cookies
    # getting the countries json list
    countries = session.get(countries_url, cookies=cookies).json()
    leaders_per_country = {}
    for country in countries:
        response = session.get(leaders_url, params={"country":country}) # change with session
        if int(str(response.status_code)[0]) > 2:
            print(f'Cookies for {country} expired! Restoring...')
            session.get(cookie_url) # updating internal cookie status
            response = session.get(leaders_url, params={"country":country}) # new cookie status passed through session
        leaders_info = response.json()
        leaders_per_country[country] = leaders_info
        for leader in leaders_info:
            # print(leader) # prints a dictionary for each leader as expected
            # print(type(leader))
            leader_intro = get_first_paragraph(leader["wikipedia_url"], session)
            leader["first_paragraph"] = leader_intro
    return leaders_per_country

def save(leaders_per_country):
    with open("leaders.json", "w", encoding="utf-8") as f:
        return json.dump(leaders_per_country, f, indent=4, ensure_ascii=False)