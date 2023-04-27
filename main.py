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
        content=[]
        response = requests.get(url)
        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'lxml')

    # get contents that wanted
            links = soup.find_all('p', class_="content-description")
            x = soup.find_all('span', class_="description")
            for link in links:
                  #href = link.get('href')
                 content.append(link.text)
            for link in x:
                  #href = link.get('href')
                 content.append(link.text)     
            return content     
        else:
             print(f'Hata kodu: {response.status_code}')         
if __name__=='__main__':
    a=[]
    for i in  usejson(data.decode("utf-8")):
      
        print(i)
        a.append(i) 
    for i in a:
          
        print(crawling(i))        
        
     