# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:11:50 2017

@author: Sun Xie
"""

import requests
from bs4 import BeautifulSoup 

url = ''
r = requests.get(url)

soup = BeautifulSoup(r.content,'lxml')

links = soup.find_all('a')

for link in links:
    print("<a href='%s'>%s</a>") %(link.get('href'), link.text)
    
g_data = soup.find_all('div',{'class':'info'})

for item in g_data:
    business_name = item.contents[0].find_all('a',{'class':'business-name'})[0].text
    
    try:
        print item.content[1].find_all('span',{'itemprop':'streetAddress'})[0].text
    except:
        pass
    
    try:
        print item.content[1].find_all('span',{'itemprop':'addressLocality'})[0].text.replace(',','')
    except: 
    
     try:
        print item.content[1].find_all('li',{'class':'primary'})[0].text
    except:
        
        
        