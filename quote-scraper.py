import requests
from bs4 import BeautifulSoup
from csv import writer


base_url = 'http://quotes.toscrape.com/'
url = '/page/1'
quote_list = []

while url:
    response = requests.get(f'{base_url}{url}')
    print(f'Now scraping {base_url}{url}')
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all(class_='quote')

    #Grab data from quotes
    for quote in quotes:
        quote_list.append({
            'text': quote.find(class_='text').get_text(),
            'author': quote.find(class_='author').get_text(),
            'bio-link': quote.find('a')['href']
        })

    #Grab next url to scrape - set it to url
    next_btn = soup.find(class_='next')
    url = next_btn.find('a')['href'] if next_btn else None

print(quote_list)
