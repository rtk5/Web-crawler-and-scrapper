import requests
from bs4 import BeautifulSoup

url = input("Enter the URL of the article you want to scrape: ")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1').get_text()

    author = soup.find('span', class_='author-name')
    author_name = author.get_text().strip() if author else "No author found"

    date = soup.find('div', class_='dateTime').get_text().strip()

    article_body = soup.find_all('p')
    content = '\n'.join([para.get_text() for para in article_body])

    print()
    print(f"Title: {title}\n")
    print(f"Author: {author_name}\n")
    print(f"Date: {date}\n")
    print(f"Content: \n{content}\n")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}\n")
