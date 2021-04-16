import urllib.error
import urllib.request
from bs4 import BeautifulSoup
from tblockref import Reference

try:
    response = urllib.request.urlopen(
        'https://terraria.fandom.com/wiki/User:Mrocza61980/sandbox')
except urllib.error.HTTPError as e:
    # Return code error (e.g. 404, 501, ...)
    print(f'{file_name} HTTPError: {e.code}')
except urllib.error.URLError as e:
    # Not an HTTP-specific error (e.g. connection refused)
    print(f'{file_name} URLError: {e.reason}')

soup = BeautifulSoup(response.read(), 'html.parser')
codelist = soup.findAll("pre")

for code in codelist:
    ref = Reference()
    blocklist = code.text.strip('\n')
    for column in blocklist.split('\n\n\n'):
        column = column.strip('\n')
        for line in column.split('\n'):
            ref.block(*line.split(' > '))
        ref.column()
    ref.out(f'output-{code["id"]}.svg')
