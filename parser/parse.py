import requests
from bs4 import BeautifulSoup
import re

url = 'http://webmineral.com/data/index.html'

proxies = {'http':'http://utmauth.ksrc.local:8080'}
response = requests.get(url,proxies = proxies)
soup = BeautifulSoup(response.text, 'lxml')
kek = []
for link in soup.findAll('a'):
    kek.append(link.get('href'))

kek2 = {}
regex = re.compile(r'IMA')
for i in kek:
    if not regex.match(i):
        #kek2.append(i)
        name = str(i).replace('.shtml','')
        kek2[name] = str(i)
#soup =soup.find_all('a',attrs='href')
#print(kek2)

a = input('Введите имя минерала\n')
print('http://webmineral.com/data/'+kek2[a])

minlink = 'http://webmineral.com/data/' + kek2[a]
#print(soup)


mineral = requests.get(minlink,proxies = proxies)
mininst = BeautifulSoup(mineral.text, 'lxml')
chem = mininst.find('b',string='Chemical  Formula: ')
formula = str(list(chem.parent.parent.findAll('td'))[1]).replace('</td>','').replace('<td>','')

print(a)
print(formula)



