import requests
from bs4 import BeautifulSoup
from typing import List, Dict

class SteamScraper:
    def __init__(self):
        self.url = "https://store.steampowered.com/search/?specials=1"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

    def get_discounted_games(self):
        
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")

       
        results = soup.find_all("a", class_="search_result_row")

        print("🎮 Discounted Games on Steam:\n")
        count = 0
        games = []
    

        for result in results:
            title = result.find("span", class_="title")
            discount_block = result.find("div", class_="discount_pct")
            price_block = result.find("div", class_="discount_final_price")
            
            dict = {
                "title": title.text.strip(),
                "discount": discount_block.text.strip(),
                "price": price_block.text.strip()
                }
            games.append(dict)
        return games

