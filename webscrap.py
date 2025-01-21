import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP request
url = "https://timesofindia.indiatimes.com/blogs/"  # Replace with the actual URL
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract data
titles = soup.find_all('h2', class_='heading1')  # Replace with actual tag and class

# Step 4: Display the titles
for title in titles:
    print(title.text.strip())




# Key Steps:
# Identify the URL: Choose the website and the data you want to scrape.
# Inspect the Web Page: Use browser developer tools (right-click > "Inspect") to locate the HTML elements containing the desired data.
# Send an HTTP Request: Use the requests library to fetch the web page content.
# Parse the HTML: Use BeautifulSoup to navigate and extract the data.
# Extract Data: Select specific elements using CSS selectors, tags, or attributes.
# Save or Process Data: Save the data in a structured format (e.g., CSV, JSON, database).
# 2. Python Libraries for Web Scraping
# Requests: To fetch the content of a webpage.
# BeautifulSoup: To parse HTML and XML documents.
# Selenium: For dynamic websites requiring JavaScript interaction.
# Scrapy: A powerful framework for large-scale scraping.
