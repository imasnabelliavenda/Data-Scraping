from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://www.bukalapak.com/products?'
params = {
    'D':'batik%20banyuwangi'
}
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
driver = webdriver.Chrome()
fullURL = f"{URL}&search%5Bkeywords%5D={params['D']}"
driver.get(fullURL)
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all('div',{'class':'bl-flex-item mb-8'})

for i in range(len(data)):
    nama = data[i].find('p', {'class':'bl-text--secondary'})
    harga = data[i].find('p', {'class':'bl-product-card-new__price'})
    
    if nama and harga:
        print("Nama produk: " + nama.text.strip())
        print("Harga: Rp." + harga.text.strip())

    link_produk = data[i].find('a', {'href':True})
    if link_produk:
        link = link_produk['href']
        driver.get(link)
        html_detail = driver.page_source
        soup_detail = BeautifulSoup(html_detail, 'html.parser')

        penjual = soup_detail.find('h3', {'class': 'c-seller__name'})
        print("Penjual: " + penjual.text, "\n")
        
        driver.back() 

driver.quit()