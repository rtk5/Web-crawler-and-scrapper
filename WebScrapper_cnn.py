import requests
from bs4 import BeautifulSoup

url = input("Enter the URL of the article you want to scrape: ")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find title
    title = soup.find('h1').get_text() if soup.find('h1') else "No title found"

    # Find author
    author = soup.find('span', class_='author-name')
    author_name = author.get_text().strip() if author else "No author found"

    # Find date
    date = soup.find('div', class_='dateTime')
    date_text = date.get_text().strip() if date else "No date found"

    # Find article body
    article_body = soup.find_all('p')
    content = '\n'.join([para.get_text() for para in article_body])

    # Print results
    print(f"\nTitle: {title}\n")
    print(f"Author: {author_name}\n")
    print(f"Date: {date_text}\n")
    print(f"Content: \n{content}\n")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}\n")
