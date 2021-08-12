import requests
from bs4 import BeautifulSoup

response = requests.get("https://habr.com/ru/all/")

text = response.text

KEYWORDS = {'дизайн', 'фото', 'web', 'python'}

soup = BeautifulSoup(text, features="html.parser")

articles = soup.find_all(class_="tm-articles-list__item")

for article in articles:
    article_mod = set(article.get_text(" ", strip=True).lower().split())
    if KEYWORDS & article_mod:
        data = article.find('time').attrs.get("title")
        title = article.find("h2").find("a").find('span').text
        link = "https://habr.com" + article.find("h2").find("a").attrs.get("href")
        print(f"{data} - {title} - {link}")
