import csv
from requests_html import HTMLSession

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['heading','summary','pictures'])

session = HTMLSession()
r = session.get('https://en.wikipedia.org/wiki/Chicken')

# Find all h2 headings (section titles)
headings = r.html.find('h2')

for heading in headings[:3]:
    print(heading.text)
    print()
    
    # Start with the next sibling of the heading
    sibling = heading.element.getnext()
    while sibling is not None and sibling.tag != 'h2':
        if sibling.tag in ['p', 'ul', 'ol']:
            print(sibling.text_content().strip())
        sibling = sibling.getnext()
    
    print()

# Find all images on the page
images = r.html.find('img')

for img in images[:5]: 
    img_url = img.attrs.get('src')
    if img_url.startswith('//'):
        img_url = 'https:' + img_url
    elif not img_url.startswith('http'):
        img_url = 'https://en.wikipedia.org' + img_url
    print(img_url)
    print()








csv_writer.writerow(['heading','summary','pictures'])
csv_file.close()