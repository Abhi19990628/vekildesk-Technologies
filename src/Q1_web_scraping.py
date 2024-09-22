# Q1_web_scraping.py
import requests
from bs4 import BeautifulSoup

def scrape_latest_articles():
    url = 'https://edition.cnn.com/world'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h3', class_='cd__headline')

    for article in articles[:10]:
        title = article.get_text()
        link = article.find('a')['href']
        if not link.startswith('https'):
            link = 'https://edition.cnn.com' + link
        print(f"Title: {title}\nURL: {link}\n")

if __name__ == "__main__":
    scrape_latest_articles()
