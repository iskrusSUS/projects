import requests
from bs4 import BeautifulSoup
import lxml

url = "https://kups.club/"

agent = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}

response = requests.get(url, headers=agent)
#print(response.status_code)

soup = BeautifulSoup(response.text, "lxml")

all_product = soup.find('div', class_='row mt-4')
list_product = all_product.find_all('div', class_='col-lg-4 col-md-4 col-sm-6 portfolio-item')
print(list_product[0].text)