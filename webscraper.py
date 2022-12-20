import requests
from bs4 import BeautifulSoup

def search_pages(url, term):
    # Retrieve the content of the page
    response = requests.get(url)
    content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    # Search for the term in the page content
    if term in soup.text:
        print(f'Found "{term}" in {url}')

# Define the URL of the website you want to search
base_url = 'https://keys.lol/bitcoin'

# Define the term you want to search for
term = '12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr'

# Search the first page
search_pages(base_url, term)

# Search the other pages, if they exist
page = 2
while True:
    # Construct the URL of the next page
    next_url = f'{base_url}?page={page}'

    # Check if the page exists
    response = requests.head(next_url)
    if response.status_code == 404:
        # Stop searching if the page does not exist
        break

    # Search the page
    search_pages(next_url, term)

    # Increment the page number
    page += 1
