import requests
from bs4 import BeautifulSoup

# URL of the Hindustan Times article
url = input("Enter the URL of the article you want to scrape: ")


# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

# Send a GET request to the webpage
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title of the article
    title = soup.find('h1').get_text()

    # Extract the author of the article
    author = soup.find('span', class_='author-name')
    author_name = author.get_text().strip() if author else "No author found"

    # Extract the date of the article
    date = soup.find('div', class_='dateTime').get_text().strip()

    # Extract the main content of the article
    article_body = soup.find_all('p')
    content = '\n'.join([para.get_text() for para in article_body])

    # Print the results
    print()
    print(f"Title: {title}\n")
    print(f"Author: {author_name}\n")
    print(f"Date: {date}\n")
    print(f"Content: \n{content}\n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}\n")
