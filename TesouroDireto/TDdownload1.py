import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
import requests
import os
#from urllib.request import urlretrieve

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'https://www.tesourotransparente.gov.br/ckan/dataset'

url = 'https://www.tesourotransparente.gov.br/ckan/dataset/taxas-dos-titulos-ofertados-pelo-tesouro-direto'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('a')
for tag in tags:
    if  '.csv' in tag.get('href', '0'):
        print('URL:', tag.get('href'))
        dl_url = tag.get('href')

#dl_file = urllib.request.urlretrieve(dl_url)
dl_file = requests.get(dl_url, params = {'downloadformat' : 'csv'})
print(dl_file.ok)


if dl_file.ok:
    #print("saving to", os.path.abspath(file_path))
    with open('TDhistory.csv', 'wb') as f:
        for chunk in dl_file.iter_content(chunk_size=1024 * 8):
            if chunk:
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())
else:  # HTTP status code 4XX/5XX
    print("Download failed: status code {}\n{}".format(dl_file.status_code, dl_file.text))

#add buys and sales