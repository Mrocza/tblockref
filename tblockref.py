import os
import re
import base64
import urllib.request, urllib.error
from jinja2 import Template
from bs4 import BeautifulSoup
from datetime import datetime



class Reference:
    def __init__(self, scale = 2, margin = 6):
        self._margin = margin
        self._scale = scale

        self._block_dict = {}
        self._height = 0
        self._width = 0
        self._column_width = 0

        self._pos_x = self._margin
        self._pos_y = self._margin

    def block(self, block_name = None, file_name = None):
        if not block_name:
            self.space()
            return

        print(f'Adding block {block_name} ...')

        if not file_name:
            file_name = block_name.replace(' ','_')+'_(placed)'
            for format in ['.png', '.gif']:
                if self._isfile(file_name + format):
                    file_name += format
                    self._getfile(file_name)
                    break
        else:
            self._getfile(file_name)

        # set data for current block
        self._block_dict[block_name] = {
            'sprite_x': str(self._pos_x),
            'sprite_y': str(self._pos_y),
            'sprite_width': str(24*self._scale),
            'sprite_height': str(24*self._scale),
            'sprite_href': 'res/'+file_name,
            'text_x': str(self._pos_x+30*self._scale),
            'text_y': str(self._pos_y+12*self._scale),
            'text_tspan': block_name
        }

        # advance to next block posiotion
        self._pos_y += 12*self._scale

        # adjust document height to the highest y value reached
        if self._height < self._pos_y + 12*self._scale:
            self._height = self._pos_y + 12*self._scale

    def space(self):
        self._pos_y += 24*self._scale

    def column(self, column_width):
        self._pos_y = self._margin # reset y value back to top
        self._pos_x += self._column_width # adjust x value by previous column width
        self._column_width = column_width # set current column width
        self._width += column_width # increase document width to fit new column

    def _isfile(self, file_name):
        try:
            urllib.request.urlopen('https://terraria.gamepedia.com/File:'+file_name)
        except urllib.error.HTTPError as e:
            # Return code error (e.g. 404, 501, ...)
            print(f'{file_name} HTTPError: {e.code}')
            return False
        except urllib.error.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused)
            print(f'{file_name} URLError: {e.reason}')
            return False
        else:
            return True

    def _getfile(self, file_name):
        # Retrieving a direct image url:
        response = urllib.request.urlopen(
            'https://terraria.gamepedia.com/File:'+file_name)
        soup = BeautifulSoup(response.read(), 'html.parser')
        image_href = soup.find("div", {"class": "fullMedia"}).a['href']
        # Getting last modification timestamp from the url parameter 'cb'
        parsed = urllib.parse.urlparse(image_href)
        mod_date_string = (urllib.parse.parse_qs(parsed.query)['cb'])[0]
        mod_date = datetime.strptime(mod_date_string, '%Y%m%d%H%M%S')
        # Getting last modification timestamp for local file
        if os.path.isfile('res/'+file_name):
            last_update = datetime.fromtimestamp(
                os.path.getmtime('res/'+file_name))
        else:
            last_update = datetime(1970,1,1)
        # Download if newer
        if mod_date > last_update:
            urllib.request.urlretrieve(image_href, 'res/'+file_name)

    def embed(self):
        for block in self._block_dict:
            with open(self._block_dict[block]['sprite_href'], "rb") as f:
                self._block_dict[block]['sprite_href'] = (
                    'data:image/png;base64,'
                    + base64.b64encode(f.read()).decode())

    def out(self, output):
        with open('svg_template.svg', 'r') as f:
            svg = Template(f.read(), trim_blocks=True, lstrip_blocks=True)
        with open(output, 'w') as f:
            f.write(svg.render(
                svg_width= self._width + self._margin,
                svg_height= self._height + self._margin,
                block_values= self._block_dict.values()
            ))
