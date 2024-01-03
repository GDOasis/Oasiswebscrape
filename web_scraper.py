# web_scraper.py
import argparse
import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Web Scraper')
    parser.add_argument('target_url', help='URL of the website to scrape')
    args = parser.parse_args()

    # Call the web_scraper function with the provided URL
    web_scraper(args.target_url)
