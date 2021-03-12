import requests as req
from bs4 import BeautifulSoup
import csv
import time

url = "https://football.ua/"
resp = req.get(url)
result = resp.content
soup = BeautifulSoup(result, 'lxml')

csv_file = open("Parse_Foot_news/main_news.csv", 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'date', 'body_text', 'link'])

# find links of the main_news section
article = soup.find('article', class_='main-news')
main_news_links = []
for link in article.find_all('li'):
    main_news_links.append(link.a['href'])


# get the title, date and body from the articles
def find_info(link):
    resp = req.get(link)
    result = resp.content
    soup = BeautifulSoup(result, 'lxml')

    art = soup.find('article', class_='author-article')
    if art is None:
        art = soup.find('article', class_='article')
        title = art.h1.text
        date = art.find('p', class_='article_date').text
        body = art.find('div', class_='article_text')
    else:
        title = art.h1.text
        date = art.find('p', class_='date').text
        body = art.find('div', class_='article-text')
    body_text = ''
    for p in body.find_all('p'):
        body_text += ''.join(p.text)

    csv_writer.writerow([title, date, body_text, link])

    # print(title)
    # print(date)
    # print(body_text)
    # print(link)


def main():
    for link in main_news_links:
        find_info(link)


if __name__ == "__main__":
    main()

print("1% done..")
time.sleep(1)
print("10% done..")
time.sleep(1)
print("39% done..")
time.sleep(1)
print("78% done..")
time.sleep(0.5)
print("99% done..")
time.sleep(2)
print("Writing complete!")
csv_file.close()

# check
