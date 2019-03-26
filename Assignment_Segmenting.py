# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"

res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')

table=soup.find('table', class_='wikitable sortable')
#table=soup.find(‘table’,{‘class’:’wikitable sortable’})

Postcode=[]
Borough=[]
Neighbourhood=[]

df=pd.DataFrame()
   
for row in table.find_all('tr'):
    data = row.find_all('td')
    try:
        Postcode.append(data[0].text)
        Borough.append(data[1].text)
        Neighbourhood.append(data[2].text)
    except IndexError:pass
    #print("{}|{}|{}".format(Postcode, Borough,Neighbourhood))
##Postcode = [x.encode("UTF8") for x in Postcode]
#Borough = [x.encode("UTF8") for x in Borough]
#Neighbourhood = [x.encode("UTF8") for x in Neighbourhood]
df['Postcode']=Postcode
df['Borough']=Borough
df['Neighbourhood']=Neighbourhood

print(df)


#convert all values from unicode to string




