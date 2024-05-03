import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import ssl
import pandas as pd

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#get data from 'https://www.tesourodireto.com.br/titulos/precos-e-taxas.htm'
#but it is not working
url = 'https://www.tesourodireto.com.br/titulos/calculadora.htm'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

print(soup)
fhand = urllib.request.urlopen('https://www.tesourodireto.com.br/titulos/calculadora.htm')
for line in fhand:
    if line.decode().strip().startswith('<td'):
        print(line.decode().strip()) #you need to decode, because url is encrypted in bytes

# Retrieve all of the anchor tags
tags = soup.findAll('span')
#print(tags)
for tag in tags:
    print(tag.text)
