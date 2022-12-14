import os
import json
import base64
import urllib.error
import urllib.request
from jinja2 import Template
from bs4 import BeautifulSoup
from datetime import datetime
from PIL import Image


output = ''
for file in os.listdir('./res'):
    extension = os.path.splitext(file)[1][1:]
    id = os.path.splitext(file)[0].replace('_(placed)','').lower()
    with Image.open('./res/' + file) as im:
        w, h = im.size
    with open('./res/' + file, "rb") as f:
        href = (
            f'data:image/{extension};base64,'
            + base64.b64encode(f.read()).decode()
        )
    x, y = 0, 0
    if w == 32:
        x, y = -4, -4
    output += f'<image id="{id}" x="{x}" y="{y}" width="{w*2}" height="{h*2}" xlink:href="{href}"/>\n'

with open('data.json', 'w') as f:
    f.write(output)
