# Importing necessary libraries
import requests
from bs4 import BeautifulSoup

# Function to scrape a website
def web_scraper(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extracting all the links from the page
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))

    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

# Example usage
if __name__ == "__main__":
    # Replace 'https://example.com' with the target website URL
    target_url = 'https://example.com'
    web_scraper(target_url)
