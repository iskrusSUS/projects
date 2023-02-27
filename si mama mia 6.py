import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.euronics.it/gaming/playstation-4/f"

agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

response = requests.get(url, headers=agent)
# print(response.status_code)

soup = BeautifulSoup(response.text, "lxml")

all_product = soup.find('div', class_='row product-grid')
list_product = all_product.find_all('div', class_='col-md-3 col-sm-3 col-xs-6 product-layout grid-mode')
print(list_product[0].text)