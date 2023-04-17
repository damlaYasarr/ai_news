import requests
from bs4 import BeautifulSoup
import http.client
import json
conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 6RstF5fE8SyIScRGurFXqn:6dmyQTG1G74VLhMQMbKE9t"
    }

conn.request("GET", "/news/getNews?country=tr&tag=general", headers=headers)

res = conn.getresponse()
data = res.read()

def usejson(data):
   
    response = json.loads(data)
    print(type(response))
    urls=[]
    for article in response['result']:
    
         url = article.get('url')
         urls.append(url)
    return urls     
def crawling(url):
        response = requests.get(url)
        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'html.parser')

    # get contents that wanted
            links = soup.find_all('a')
            for link in links:
                  href = link.get('href')
                  print(href)
        else:
             print(f'Hata kodu: {response.status_code}')         
if __name__=='__main__':
    a=[]
    for i in  usejson(data.decode("utf-8")):
        a.append(i) 
    for i in a:
            
        crawling(i)        