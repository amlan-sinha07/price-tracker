from bs4 import BeautifulSoup
import requests
import time
from urllib.parse import urlparse
def validate_url(url):
    parsed=urlparse(url)
    if parsed.scheme not in ("http","https"):
        raise ValueError("Only http and https urls are supported")
    if not parsed.netloc or not parsed.hostname:
        raise ValueError("Invalid url: hostname is missing")
    return True
def fetch_page(url):
    validate_url(url)
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    return response.text
def scrape_books(url):
    response=requests.get(url)
    response.raise_for_status() #if website is down this helps
    response.encoding='utf-8'
    soup=BeautifulSoup(response.text,"html.parser")
#book_name=soup.find('h3').find('a').get('title')
#price=soup.find('p',class_='price_color').text.strip()
    books=soup.find_all('article',class_='product_pod')
    results=[]
    for book in books:
        book_name=book.find('h3').find('a').get('title')
        price=book.find('p',class_='price_color').text.strip()
        available=book.find('p',class_="instock availability").text.strip()
        book_data={
            "books_name":book_name,
            "Price":price,
            "Availability":available
        }
        results.append(book_data)
    return results

    #print(f"Books_name = {book_name} \nPrice = {price}\nAvailability = {available}")
def scrape_all_pages(base_url,max_pages=5):
    all_books=[]
    for page_num in range(1,max_pages+1):
        url=f"{base_url}/catalogue/page-{page_num}.html"
        books=scrape_books(url)
        if not books:
            break
        all_books.extend(books)
        time.sleep(1)
    return all_books
if __name__=="__main__":
    BASE_URL="https://books.toscrape.com"
    #BASE_URL="https://www.flipkart.com/apple-iphone-17-pro-max-cosmic-orange-256-gb/p/itm81f3a173391c4?pid=MOBHFN6YQKMWVPXH&param=23456789&BU=Mobile&pageUID=1793979890390"
    #BASE_URL="https://www.flipkart.com"
    data=scrape_all_pages(BASE_URL,max_pages=3)
    print(len(data))
    print("first book")
    print(data[0])
    print(data[20])
    #for book in data:
     #   print(book)