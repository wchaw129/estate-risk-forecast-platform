import requests as r
from bs4 import BeautifulSoup
import time

class Scraper:
    def __init__(self, transaction_type: str = 'sprzedaz', estate_type: str = 'mieszkanie', province: str = 'dolnoslaskie', city: str = 'wroclaw'):
        self.transaction_type = transaction_type
        self.estate_type = estate_type
        self.province = province
        self.city = city

        self._base_url = "https://www.otodom.pl/pl/wyniki"
        self._headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    
    
    @property
    def url(self) -> str:
        return (
            f"{self._base_url}/{self.transaction_type}/{self.estate_type}/{self.province}/"
            f"{self.city}?limit=72&ownerTypeSingleSelect=ALL&by=LATEST&direction=DESC"
        )
    
    
    
    def download_test_page(self, file_name: str = 'example.html'):
        response = r.get(self.url, headers=self._headers)
        response.raise_for_status()
        with open('tests/'+file_name, 'w', encoding='utf8') as file:
            file.write(response.text)
    
    
    def run(self, offline: bool = False):
        
        if offline: 
            with open('example.html', 'r', encoding='utf8') as file:
                html_content = file.read()
            #TODO

        #response = r.get(self.url, headers=self._headers)
        #response.raise_for_status()



        soup = BeautifulSoup(html_content, 'html.parser')
        code = soup.find('div', {'data-cy': 'search.listing.organic'}).find_all('article', {'data-sentry-element': 'Container'})

        res = {}
        for ad in code:
            if ad.get('role') == None:
                name = ad.find('p', {'data-cy': 'listing-item-title'}).get_text()
                price = ad.find('span', {'data-sentry-element': "MainPrice"}).get_text()
                rooms_size_floor = ad.find('dl', {'data-sentry-element': "StyledDescriptionList"}).find_all('span')
                if len(rooms_size_floor) == 3:
                    rooms, size, floor = [i.get_text() for i in rooms_size_floor]
                else:
                    rooms, size = [i.get_text() for i in rooms_size_floor]
                    floor = None
                place = ad.find('p', {'data-sentry-component': 'Address'}).get_text()
                res[name]=[price, place, rooms, size, floor]
        return res
    
if __name__ == "__main__":
    scraper = Scraper()
    scraper.download_test_page()
    