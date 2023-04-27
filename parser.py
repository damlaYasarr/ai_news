import json
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup


def loadRSS():
      
    # url of rss feed
    linkmain='https://www.trthaber.com/xml_mobile.php?tur=xml_genel&kategori=&adet=20&selectEx=yorumSay,okunmaadedi,anasayfamanset,kategorimanset'

    # creating HTTP response object from given url
    resp = requests.get(linkmain)
  
    # saving the xml file
    with open('xml_genel.xml', 'wb') as f:
        f.write(resp.content)

def xmlparsing(xmlfile):
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot()
    print(root)
    # create empty list for news items
    newsitems = []
    count=0
    # iterate news items
    for item in root:
        print(item)
        
        count+=1
        # empty news dictionary
        news = {}
  
        # iterate child elements of item
        for child in item:
            if child.tag == 'haber_link':
                news['haber_link'] = 'https://www.trthaber.com/'+child.text
            if child.tag == 'haber_manset':
                news['haber_aciklama'] = child.text.replace('\"','')
            if child.tag == 'haber_metni':
                
                news['haber_metni'] = tagparser(["p", "\n\t"],child.text)
                
     
        # append news dictionary to news items list
        newsitems.append(news)
    print(count)
    # return news items list
    
        
    return newsitems
def tagparser(tag, text):
    newtext=[]
    soup = BeautifulSoup(text, 'html.parser')
    paragraphs = soup.find_all(tag)
    for p1, p2 in zip(paragraphs, paragraphs[1:]):
        if str(p1.next_sibling) == '\n\t'  and str(p2.next_sibling) == '\n\t':
            newtext.append(p1.text)
        else:
            newtext.append(p1.text)
    newtext.append(paragraphs[-1].text)  # add last paragraph
  
    newtext = [item.strip().replace('\n\t\t','') for item in newtext]
    newtext = [item.strip().replace('\n\t','') for item in newtext]
    newtext = [item.strip().replace('\n','') for item in newtext]
    newtext = [item.strip().replace('\"','') for item in newtext]
    
    text=" ".join(newtext)
    return text
def savetoJson(newsitems, filename):
    with open(filename, 'w',encoding='utf-8') as f:
        json.dump(newsitems, f,  ensure_ascii=False,indent=4)
  
if __name__=='__main__':
    loadRSS()
  
    # parse xml file
    newsitems = xmlparsing(r'C:\Users\damla\Desktop\ai\xml_genel.xml') 
    savetoJson(newsitems, 'content.json')  