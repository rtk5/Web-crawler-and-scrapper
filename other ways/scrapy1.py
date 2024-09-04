from requests_html import HTMLSession

# Initialize a session
session = HTMLSession()

# Get the webpage content
response = session.get('https://www.geeksforgeeks.org/html-tutorial/?ref=shm')

# Parse the HTML content
html = response.html

# Find all article sections
articles = html.find('div.tutorial-content-div')  # Update this selector based on actual HTML structure

# Loop through each article and extract the headline and summary
for article in articles:
    headline = article.find('h2', first=True).text if article.find('h2', first=True) else 'No headline found'
    summary = article.find('p', first=True).text if article.find('p', first=True) else 'No summary found'
    print(headline)
    print(summary)
    print()
