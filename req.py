import urllib2
import pprint
from bs4 import BeautifulSoup
import json

url=urllib2.urlopen("http://www.hmc.iitkgp.ac.in/web/boarders-list-ug/")

content=url.read()

soup=BeautifulSoup(content,"html.parser")
data=[]
table=soup.find_all('table',id="boarderUG")
target=open("write.txt","w")
for line in table:
    for row in line.find_all('tr'):
        d=[]
        for col in row.find_all('td'):
            d.append(col.text)
        data.append(d[1:])
result=[]

for row in data[1:]:
    dictt={}
    dictt=dict(roll=row[0],name=row[1],hall=row[2],room=row[3],stat=row[4])
    result.append(dictt)

with open('data.json','w') as out:
    json.dump(result,out)
pp=pprint.PrettyPrinter(indent=3)
pp.pprint(json.dumps(result))
print("Parsing Successful")
