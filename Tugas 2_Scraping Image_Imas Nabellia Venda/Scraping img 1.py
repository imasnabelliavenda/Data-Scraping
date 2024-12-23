import requests
from bs4 import BeautifulSoup

url = 'https://eksepsionline.com/category/sastra/cerpen/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all('img')

for img in data:
    print(img.get('src'))