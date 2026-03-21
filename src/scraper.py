import requests as r
from bs4 import BeautifulSoup
import time
import pandas as pd

class Scraper:
    def __init__(self, transaction_type: str = 'sprzedaz', 
                 estate_type: str = 'mieszkanie', 
                 market_type: str = 'rynek-wtorny',
                 province: str = 'dolnoslaskie', 
                 city: str = 'wroclaw'):
        
        self.transaction_type = transaction_type
        self.estate_type = estate_type
        self.market_type = market_type
        self.province = province
        self.city = city

        self._base_url = "https://www.otodom.pl/pl/wyniki"
        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    
    
    @property
    def url(self) -> str:
        """get url based on the filter"""
        return (
            f"{self._base_url}/{self.transaction_type}/{self.estate_type},{self.market_type}/{self.province}/"
            f"{self.city}?limit=72&ownerTypeSingleSelect=ALL&by=LATEST&direction=DESC"
        )
    
    
    def download_test_page(self, file_name: str = 'example.html'):
        """downloads test page from otodom with .html format"""
        response = r.get(self.url, headers=self._headers)
        response.raise_for_status()
        with open('tests/'+file_name, 'w', encoding='utf8') as file:
            file.write(response.text)
    
    def open_test_page(self, file_name: str = 'example.html'):
        with open('tests/'+file_name, 'r', encoding='utf8') as file:
            return file.read()

    def scrape(self, html_content):
        """scraping of the html page given"""
        soup = BeautifulSoup(html_content, 'html.parser')
        code = soup.find('div', {'data-cy': 'search.listing.organic'}).find_all('article', {'data-sentry-element': 'Container'}) 
        
        res = {}
        # loop for every advertisement on the site
        for ad in code:
            if ad.get('role') == None: 
                name = ad.find('p', {'data-cy': 'listing-item-title'}).get_text()  
            elif ad.get('role') == 'presentation':
                name = ad.find('p', {'data-sentry-element': 'Title'}).get_text()
            else: 
                name = None  
            place = ad.find('p', {'data-sentry-component': 'Address'}).get_text()
            price = ad.find('span', {'data-sentry-element': "MainPrice"}).get_text()
            rooms_size_floor = ad.find('dl', {'data-sentry-element': "StyledDescriptionList"}).find_all('span')
            if len(rooms_size_floor) == 3:
                rooms, size, floor = [i.get_text() for i in rooms_size_floor]
            else:
                rooms, size = [i.get_text() for i in rooms_size_floor]
                floor = None

            res[name]=[price, place, rooms, size, floor]

        return res

    def run(self):
        """running scraping of every available page based on the filter settings"""
        response = r.get(self.url, headers=self._headers)
        response.raise_for_status()
        # TODO
    
if __name__ == "__main__":
    scraper = Scraper()
    content = scraper.open_test_page()
    result = scraper.scrape(content)
    df = pd.DataFrame.from_dict(result, orient='index')
    print(df)