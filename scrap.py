# -*- coding: utf-8 -*-
# python3 -m pip install BeautifulSoup4
import re
import urllib.request
from bs4 import BeautifulSoup
URL= input("URL: ")
profundidad=input("profundidad: ")
result=[]
listaSitio=[]
ii=0
datos=""
def navega(pag):
	print(pag)
	datos = urllib.request.urlopen(pag).read().decode('latin-1')
	soup =  BeautifulSoup(datos)
	tags = soup("a")
	for tag in tags:
		if (re.search("@",str(tag.get("href")))):
			pass
		elif (re.search("#",str(tag.get("href")))):
			pass
		elif (re.search(pag,str(tag.get("href")))):
			listaSitio.append(tag.get("href"))
		elif (re.search("http",str(tag.get("href")))):
			pass
		else:
			concat=pag+str(tag.get("href")) 
			try:
				urllib.request.urlopen(concat).read().decode('latin-1')
				listaSitio.append(concat)
			except:
				pass

while (ii<=int(profundidad)):	
	print ("Nivel:"+str(ii))
	navega(URL)
	for sitio in listaSitio:
		navega(sitio)
	ii=ii+1

for item in listaSitio:
    if item not in result:
        result.append(item)
	
for i in result:
	print(i.decode('latin-1'))