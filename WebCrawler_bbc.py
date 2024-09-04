import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

class WebCrawler:
    def __init__(self, base_url, max_depth):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited = set()

    def crawl(self, url, depth):
        if depth > self.max_depth or url in self.visited:
            return

        try:
            response = requests.get(url)
            if response.status_code != 200:
                return
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            return

        self.visited.add(url)
        print(f"Crawling: {url}, Depth: {depth}")

        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            full_url = urljoin(url, link['href'])
            if full_url.startswith(self.base_url):
                self.crawl(full_url, depth + 1)
        
        time.sleep(1)

    def start_crawling(self):
        self.crawl(self.base_url, 0)

if __name__ == "__main__":
    base_url = "https://www.bbc.com/news"  
    max_depth = 2  
    crawler = WebCrawler(base_url, max_depth)
    crawler.start_crawling()
