from bs4 import BeautifulSoup
import requests
response=requests.get("https://books.toscrape.com")
response.raise_for_status() #if website is down this helps
response.encoding='utf-8'
soup=BeautifulSoup(response.text,"html.parser")
#book_name=soup.find('h3').find('a').get('title')
#price=soup.find('p',class_='price_color').text.strip()
books=soup.find_all('article',class_='product_pod')
for book in books:
    book_name=book.find('h3').find('a').get('title')
    price=book.find('p',class_='price_color').text.strip()
    available=book.find('p',class_="instock availability").text.strip()
    print(f"Books_name = {book_name} \nPrice = {price}\nAvailability = {available}")