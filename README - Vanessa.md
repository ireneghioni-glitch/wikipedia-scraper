# Wikipedia Scraper (Pair Programming Edition)

- Repository: `wikipedia-scraper`
- Type: `Consolidation & Collaboration`
- Duration: `3 days`
- Deadline: `02/06/2026 4:30 PM`
- Team: `2 learners`

## Mission Objectives

In this project, you and your partner will collaborate to:

1. Create a shared, isolated development environment.
2. Build a modular Python application using **Git Flow** best practices (feature branches, Pull Requests, code reviews).
3. Query a REST API to retrieve information and modularize the API client.
4. Build a targeted web scraper using BeautifulSoup to extract and sanitize unstructured web data.
5. Combine your modules into a high-performance script using multiprocessing.

Scraping and data collection are core data engineering tasks. Doing this as a team simulates how production data pipelines are built in the real world.

![scraping](https://media4.giphy.com/media/Xe02toxlUsztG7iQgb/giphy.gif?cid=ecf05e47lixeo6qe5y4ooabkh0hfdz0t1pio4h0qgbngjq0n&ep=v1_gifs_search&rid=giphy.gif&ct=g)

## Learning Objectives

- Get familiar with GitHub workflows best practices (branching, pull-requests, merging)
- Use [venv](https://docs.python.org/3/library/venv.html) to isolate your Python environment
- Use [requests](https://requests.readthedocs.io/en/latest/) to call an external API are any internet link
- Use [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to extract text from HTML
- Use proper exception handling
- Get comfortable with JSON 
- (_Optional_) Use OOP to split functionalities into classes and methods
- (_Optional_) Use regex to clean text data
- (_Optional_) Use multiprocessing to speedup your code

---

## Repo Architecture & Git Flow

To avoid stepping on each other's toes, your repository structure **must** look like this:

```text
wikipedia-scraper/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── dev/
│   ├── student_a_sandbox.ipynb
│   └── student_b_sandbox.ipynb
└── src/
    ├── __init__.py
    ├── api_client.py
    └── html_scraper.py
```
## 🛑 Strict Collaboration Rules
- Protect the Main Branch: Nobody pushes directly to main. All development must happen on descriptive feature branches (e.g., feature/api-client, feature/html-scraper).
- Peer-Reviewed Pull Requests: When a feature is ready, open a Pull Request (PR). Your partner must review, comment on, and approve the code before it is allowed to merge into main.
- Isolated Playgrounds: Use your designated notebook inside the dev/ directory for initial API testing and layout exploration. This keeps your experimental code out of the production module files.

## The Mission

Create a scraper that builds a JSON file with the political leaders of each country you get from this API: [https://country-leaders.onrender.com/docs](https://country-leaders.onrender.com/docs).

Include in this file the first paragraph of the Wikipedia page of these leaders (you'll retrieve the Wikipedia page URL from the API, which you then have to scrape yourself).

## Recommended Timeline (3 Days)
- Day 1: Phase 0 (Setup, API exploration, and notebook prototyping).
- Day 2: Phase 1 (Building production modules on separate feature branches + PR reviews).
- Day 3: Phase 2 & Bonuses (Integration in main.py, testing, and documentation).

### Phase 0: Setup & Sandbox Exploration

- Student A creates the GitHub repository and invites Student B as a collaborator. Do initialize with a README.md. They create a dev/ folder and add two copies of the sandbox notebook.

- Both partners clone the repository locally, spin up a venv, and ensure it is covered by the .gitignore.
- Each learner uses their personal notebook guide to investigate the API endpoints, study cookie behavior, and test BeautifulSoup selectors. **Read the docs from the [API](https://country-leaders.onrender.com/docs)!**
- Once each learner has the logic of the code completed in the notebook guide, discuss how will you address Phase 1 below.

### Phase 1: Parallel Modular Development

Divide the core architecture into two parallel tracks. One student owns the API client interface, while the other owns the HTML text processing engine. Create separate git feature branches for these tracks.

#### Track 1: The API Client (src/api_client.py)
- Build a CountryLeadersAPI class responsible only for communicating with the REST API.
    - Attributes: base_url, country_endpoint, leaders_endpoint, cookies_endpoint, and session (optional: utilizing a persistent requests.Session()).
    - Methods:
        - refresh_cookie(): Checks validity and refreshes the session cookie when expired.
        - get_countries(): Queries the API and returns a clean list of supported country codes.
        - get_leaders(country: str): Fetches and returns the raw JSON list of leaders for a targeted country.

####  Track 2: The HTML Scraper (src/html_scraper.py)
- Build a WikipediaScraper class responsible only for downloading and parsing HTML documents.
- Attributes: session (passed down from the parent application context).
- Methods:
    - fetch_html(url: str): Safely requests raw HTML text. Must include robust exception handling to deal with 404s, 500s, or connection drops.
    - get_first_paragraph(html: str): Parses raw HTML with BeautifulSoup, finds the first true biographical narrative paragraph (<p>), and returns it.
    - clean_text(text: str): A cleaning utility method to strip out unwanted characters, whitespace, or Wikipedia citation brackets (e.g., [1], [citation needed]).
    -  `to_json_file(filepath: str) -> None` stores the data structure into a JSON file
    
#### Phase 2: Integration & Orchestration (main.py)
Once both feature branches have been reviewed, approved, and merged into main, create a collective branch named feature/integration. Work together to compose the main entry script.Your main.py should act as the coordinator:
- Initialize the CountryLeadersAPI module.Retrieve the active countries and extract their leaders.
- Pass the discovered Wikipedia URLs to the WikipediaScraper engine to parse the bios.
- Map the scraped text back into the leader datasets and save the output.

## Must-Have Features (MVP)
- Production-ready src/api_client.py and src/html_scraper.py object scripts.
- A central main.py controller file that executes the entire pipeline end-to-end.
- Custom error handling to handle dropped connections or missing pages gracefully.
- A clear Git commit timeline proving active branch usage and formal PR sign-offs.

## Nice-to-Have Features (Bonuses)
- Multiprocessing: Use Python’s multiprocessing or concurrent.futures within main.py to scrape the Wikipedia URLs in parallel, speeding up execution.
- Dynamic File Exporter: Add a toggle parameter or command-line flag allowing main.py to output data as either a .json file or a flattened .csv.
- Logging System: Replace simple print() checks with Python's native logging library to track runtime warnings and pipeline stages.

## Deliverables
- 1. Publish your source code on your personal GitHub repository
    - Collaboration Proof: A history of Pull Requests, peer review logs, and branch mergers on GitHub.
    - Data Outputs: Valid leaders_data.json or leaders_data.csv files generated by executing python main.py.
- 2. Pimp up the README file
   - Description
   - Installation
   - Usage
   - Visuals
   - ... anything else you find useful
3. Show case your repo! We will pseudo-randomly 2-3 colleagues to share their work during Friday's debrief (4:30 PM).

## Evaluation

| Criterion      | Indicator                                                    | Yes/No |
| -------------- | ------------------------------------------------------------ | ------ |
| 1. Is complete | Executes whithout errors                                     |        |
|                | Stores the correct information from the API in the file      |        |
| 2. Is correct  | The code is well typed                                       |        |
|                | Good usage of OOP                                            |        |
| 3. Is great    | Possibility to store output as a CSV file                    |        |
|                | Correct usage of `Session()`                                 |        |
|                | Multi-processing                                             |        |

## You got this!

![You've got this!](https://media.tenor.com/Y56BShm-6V0AAAAi/wikipedia-wikipedian.gif)