import urllib.error
import urllib.request
from bs4 import BeautifulSoup
from tblockref import Reference

response = urllib.request.urlopen(
        'https://terraria.fandom.com/wiki/User:Mrocza61980/sandbox')

soup = BeautifulSoup(response.read(), 'html.parser')
codelist = soup.findAll("pre")

for code in codelist:
    ref = Reference(margin = 10)
    blocklist = code.text.strip('\n')
    for column in blocklist.split('\n\n\n'):
        column = column.strip('\n')
        for line in column.split('\n'):
            ref.block(*line.split(' > '))
        ref.column()
    ref.out(f'output-{code["id"]}.svg')
