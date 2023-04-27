import json
import requests
import xml.etree.ElementTree as ET



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
                news['haber_link'] = child.text
            if child.tag == 'haber_manset':
                news['haber_aciklama'] = child.text
            if child.tag == 'haber_metni':
                news['haber_metni'] = child.text
     
        # append news dictionary to news items list
        newsitems.append(news)
    print(count)
    # return news items list
    return newsitems
def savetoJson(newsitems, filename):
    with open(filename, 'w',encoding='utf-8') as f:
        json.dump(newsitems, f,  ensure_ascii=False,indent=4)
  
if __name__=='__main__':
    #loadRSS()
  
    # parse xml file
    newsitems = xmlparsing(r'C:\Users\damla\Desktop\ai\xml_genel.xml') 
    savetoJson(newsitems, 'content.json')  