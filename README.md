# Wikipedia Scraper
## Project 

## 🏢 Description
An application that retrieves political leaders from a REST API and scrapes their Wikipedia pages to extract biographical information. Built as a pair programming project using Git Flow, API integration, and web scraping techniques.

## 🚀 Project Overview
This project combines:

A REST API client to fetch countries and political leaders
A Wikipedia web scraper using BeautifulSoup
A data pipeline that merges structured API data with unstructured web data
Optional parallel processing for performance optimization

Final output: a structured JSON (or CSV) file containing leaders and their Wikipedia first paragraph.

## Features:
Core Features (MVP)
Fetch list of countries from API
Retrieve political leaders per country
Extract Wikipedia URLs from API data
Scrape Wikipedia pages
Extract and clean the first biography paragraph
Export results to JSON

## Project Structure
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

## 🧩 Modules

src/api_client.py

Handles all API communication:

Fetch countries
Fetch leaders per country
Manage session cookies
Handle API errors gracefully
src/html_scraper.py

Handles all scraping logic:

Download HTML pages
Parse Wikipedia content
Extract first meaningful paragraph
Clean extracted text


This project follows Git Flow best practices:

main → production-ready code
feature/api-client → API module development
feature/html-scraper → scraping module development
feature/integration → final orchestration

## 🧑‍💻 Authors
Neha – API module & integration
Irene – Scraper module & parsing logic

