import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

bookUrl = 'https://books.toscrape.com/'
bookHeader = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}
bookResp = rq.get(url=bookUrl, headers=bookHeader)
bookSoup = BeautifulSoup(bookResp.content, 'html.parser')
# print(bookSoup)
bookName = bookSoup.find_all('h3')
book = [book.find('a')['title'] for book in bookName]
bookDf = pd.DataFrame(book,columns=['Book Title'])
bookDf.to_csv('bookTitle.csv')