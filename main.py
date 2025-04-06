from bs4 import BeautifulSoup
import requests

# Send a GET request to the URL
url = "https://example.com"  # Replace with your target URL
response = requests.get(url)

# Print the response content
soup = BeautifulSoup(response.text, 'html.parser')  # Create a BeautifulSoup object to parse the HTML
title = soup.title.string  # The title tag contains the title of the page
print(f"Page Title: {title}")