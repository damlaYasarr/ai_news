from bs4 import BeautifulSoup
import requests
html_tt = requests.get('https://www.hurriyet.com.tr/veri-politikasi/')
html_content = html_tt.text 
soup = BeautifulSoup(html_content, 'html.parser')

a_elements = soup.find_all('div', class_='pageSub_area')

for a in a_elements:
    print(a.p.text)       