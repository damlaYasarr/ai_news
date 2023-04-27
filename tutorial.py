

#a_elements = soup.find_all('div', class_='pagebreak')

import requests
from bs4 import BeautifulSoup

url = 'https://www.hurriyet.com.tr/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

urls = []

for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.startswith('http') and '/gundem/' in href:  # filtreleme yaparak sadece haber linklerini alın
        urls.append(href)

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content=[]
    linkks=[]
    for link in soup.find_all('a'):
        href = link.get('href') 
        linkks.append(href)
 


print(linkks)         
  
def crawling():
    url = 'https://www.hurriyet.com.tr/gundem/son-dakika-haberi-van-da-7-2-buyuklugunde-deprem-41637009'

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

# haber başlığı
    title = soup.find('h1', class_='news-title').text.strip()

# haber metni
    content = ''
    for paragraph in soup.find_all('p', class_='news-text'):
        content += paragraph.text.strip() + '\n'

# haber tarihi
    date = soup.find('span', class_='news-date').text.strip()

    print('Başlık:', title)
    print('Metin:', content)
    print('Tarih:', date)       
    
if __name__=='__main__':
    
    
    crawling()   