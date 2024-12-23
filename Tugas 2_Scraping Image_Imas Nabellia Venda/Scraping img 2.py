import os, requests, MainFungsi
from bs4 import BeautifulSoup

url = 'https://eksepsionline.com/category/sastra/cerpen/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all('img')

images = []

for img in data:
    img_url =  img.get('src')
    if img_url is not None and img_url.endswith(('.jpg', '.png', '.jpeg', '.webp')):
        images.append(img_url)

print(images)

direktori = "Hasil Gambar"
MainFungsi.CreateDirectory(direktori)

for gmb in images:
    response = requests.get(gmb)
    fileName = os.path.basename(gmb)
    MainFungsi.WriteToFile2(direktori, fileName, response)
    print(response)
    print(fileName)
