from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://en.wikipedia.org/wiki/Chicken')

# for link in r.html.links:
#     print(link)

for link in r.html.absolute_links:
    print(link)