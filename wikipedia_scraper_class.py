import requests


class WikipediaScraper:

    HEADERS = {"User-Agent":"Wikipedia Scraper Project (https://github.com/ireneghioni-glitch/wikipedia-scraper/tree/main)"}
    
    PATTERN_CITATIONS = re.compile(r"\[\d+\]")
    PATTERN_PARENTHESES = re.compile(r"\(^()}*\)")
    CLEANUP_MAP = {
        re.compile(r"\s+,"): ",",
        re.compile(r"\s+\."): ".",
        re.compile(r"[ⓘ·]"): "",
        re.compile(r"\s+"): " "
    }

    def __init__(self, session:Sesion):
        self.session = session
        self.scraped_data = []

    def fetch_html(self, url:str):
        """
        Safely requests raw HTML text. 
        Must include robust exception handling to deal with 404s, 500s, or connection drops.
        """
        try:
            response = self.session.get(url, headers=WikipediaScraper.HEADERS, timeout=10)
            response.raise_for_status() # will give an int: 200 or 404 or 500
            html = response.text
            return html
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
        soup = BeautifulSoup(html, "html.parser")
        for p_tag in soup.find_all("p"):
            raw_text = p_tag.text.strip()
            if raw_text:
                return self.clean_text(raw_text)
        return "" # if no paragraph is found
        
    def clean_text(self, text: str):
        """
        A cleaning utility method to strip out 
        unwanted characters, whitespace, or Wikipedia citation brackets 
        (e.g., [1], [citation needed]).
        """
        # applies on nested parentheses
        while WikipediaScraper.PATTERN_PARENTHESES.search(text):
            text = WikipediaScraper.PATTERN_PARENTHESES.sub("", text)
        
        # applies on indices
        text = WikipediaScraper.PATTERN_CITATIONS.sub("", text)

        # applies other cleanup in the dict as class argument
        for pattern, replacement in WikipediaScraper.CLEANUP_MAP.items():
            text = pattern.sub(replacement, text)
        
        return text.strip()
    
    def to_json_file(self, filepath: str) -> None:
        """
        Stores the data structure into a JSON file.
        """
        # def save(leaders_per_country):
        # with open("leaders.json", "w", encoding="utf-8") as f:
        #     return json.dump(leaders_per_country, f, indent=4, ensure_ascii=False)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(self.scraped_data, f, indent=4, ensure_ascii=False)
            print(f'Data have been succesfully saved in {filepath}.')
        except IOError as e:
            print(f'Error during file {filepath} saving.')