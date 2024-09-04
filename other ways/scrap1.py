import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/Chicken"

# Send a request to fetch the content of the page
response = requests.get(url)

# Parse the content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the page
title = soup.find('title').get_text()

# Extract the introductory paragraph(s)
intro_paragraphs = soup.find_all('p', limit=2)  # Adjust limit based on how many paragraphs you want to extract

# Print the title
print(f"Title: {title}\n")

# Print the introductory paragraph(s)
for idx, para in enumerate(intro_paragraphs, 1):
    print(f"Intro Paragraph {idx}: {para.get_text().strip()}\n")

# Extract the main menu items
main_menu_items = soup.select('#vector-main-menu .vector-menu-content-list li a')

# Print the main menu items
print("Main Menu:")
for item in main_menu_items:
    print(f"- {item.get_text()} ({item['href']})")
