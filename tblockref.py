import os
import json
import base64
import urllib.error
import urllib.request
from jinja2 import Template
from bs4 import BeautifulSoup
from datetime import datetime

class Reference:
    def __init__(self, scale = 2, margin = 6):
        self._margin = margin
        self._scale = scale
        # Nominally the svg font used here is about 1024pt in size.
        # Number listed below brings it down to about 12pt (with scale = 2).
        self._text_scale = 0.00586 * scale

        self._block_dict = dict()
        self._height = int()
        self._width = int()

        # First slot in the reference starts off of the margin values.
        self._pos_x = self._margin
        self._pos_y = self._margin

        # Reading font data.
        with open('font_data.json', 'r') as f:
            self._font_data = json.load(f)

    def block(self, block_name = None, file_name = None):
        """
        Places a block into the reference in current position and advances to
        the next slot.
        """
        if not block_name:
            # If block name is not specified advances two slots forward creating
            # a gap in the current column. One slot is 12px wide.
            self._pos_y += 24 * self._scale
            return

        print(f'Adding block {block_name} ...')

        if not file_name:
            # If the filename is not specified a guess is made based on block
            # name with both png and gif extensions tested.
            file_name = block_name.replace(' ','_') + '_(placed)'
            for format in ['.png', '.gif']:
                if self._getfile(file_name + format):
                    file_name += format
                    break
        else:
            self._getfile(file_name)

        # List of unicode codes for each character in blockname.
        # This is neccessary for font handling.
        unicode_list = [str(ord(char)) for char in block_name]

        # Setting data for current block
        self._block_dict[block_name] = {
            'sprite_href': 'res/'+file_name,
            'sprite_x': self._pos_x,
            'sprite_y': self._pos_y,
            # Sprites have a nominal resolution of 24x24 px.
            'sprite_width': 24 * self._scale,
            'sprite_height': 24 * self._scale,
            # text is shifted 30px right and 11px down from sprite position
            'text_x': self._pos_x + 30*self._scale,
            'text_y': self._pos_y + 11*self._scale,
            'text_tspan': block_name,
            'text_tspan_unicode_list': unicode_list,
            'text_tspan_width': sum(
                [int(self._font_data[id]['horiz-adv-x']) * self._text_scale
                for id in unicode_list]
            )
        }

        if self._iswall(block_name):
            self._block_dict[block_name]['sprite_x'] -= 4 * self._scale
            self._block_dict[block_name]['sprite_y'] -= 4 * self._scale
            self._block_dict[block_name]['sprite_width'] = 32 * self._scale
            self._block_dict[block_name]['sprite_height'] = 32 * self._scale

        # Advancing to next slot position. One slot is 12px wide.
        self._pos_y += 12*self._scale

        # Adjusting document height to the highest y value reached.
        if self._height < self._pos_y + 12*self._scale:
            self._height = self._pos_y + 12*self._scale

    def column(self):
        """
        Creates a new column in the chart.
        """
        # Resetting y value back to top.
        self._pos_y = self._margin
        # Checking max name width in the column and advancing position.
        name_widths = [self._block_dict[block_name]['text_tspan_width']
            for block_name in self._block_dict]
        self._pos_x += max(name_widths) + 27*self._scale + self._margin
        # Resetting widths to not interfere with future columns.
        for block_name in self._block_dict:
            self._block_dict[block_name]['text_tspan_width'] = 0
        # Increasing document width to fit new column.
        self._width = self._pos_x

    def _getfile(self, file_name, local_only = True):
        """
        Gets a direct image link from the wiki and downloads that image if the
        modification date is newer than for the locally stored resource.
        Returns True if succesful and False when it fails.
        """
        if local_only and os.path.isfile('res/' + file_name):
            return True

        try:
            response = urllib.request.urlopen(
                'https://terraria.gamepedia.com/File:'+file_name)
        except urllib.error.HTTPError as e:
            # Return code error (e.g. 404, 501, ...)
            print(f'{file_name} HTTPError: {e.code}')
            return False
        except urllib.error.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused)
            print(f'{file_name} URLError: {e.reason}')
            return False

        # Retrieving a direct image url.
        soup = BeautifulSoup(response.read(), 'html.parser')
        image_href = soup.find("div", {"class": "fullMedia"}).a['href']
        # Getting last modification timestamp from the url parameter 'cb'.
        parsed = urllib.parse.urlparse(image_href)
        mod_date_string = (urllib.parse.parse_qs(parsed.query)['cb'])[0]
        mod_date = datetime.strptime(mod_date_string, '%Y%m%d%H%M%S')
        # Getting last modification timestamp for local file.
        if os.path.isfile('res/'+file_name):
            last_update = datetime.fromtimestamp(
                os.path.getmtime('res/'+file_name)
            )
        else:
            last_update = datetime(1970,1,1)
        # Downloading if newer.
        if mod_date > last_update:
            urllib.request.urlretrieve(image_href, 'res/'+file_name)
        return True

    def _iswall(self, block_name):
        for i in ['Wall', 'Stained', 'Fence', 'Sail']:
            if i in block_name: return True
        return False

    def out(self, output):
        """
        Outputs a completed reference to a specified file.
        """
        # Embedding all images into the file.
        for block in self._block_dict:
            extension = os.path.splitext(self._block_dict[block]["sprite_href"])[1][1:]
            with open(self._block_dict[block]['sprite_href'], "rb") as f:
                self._block_dict[block]['sprite_href'] = (
                    f'data:image/{extension};base64,'
                    + base64.b64encode(f.read()).decode()
                )

        # Loading font information and template.
        with open('svg_template.svg.jinja', 'r') as f:
            svg = Template(f.read(), trim_blocks=True, lstrip_blocks=True)
        # Rendering template and writing to file.
        with open(output, 'w') as f:
            f.write(svg.render(
                svg_width = self._width + self._margin,
                svg_height = self._height + self._margin,
                block_values = self._block_dict.values(),
                svg_glyphs = self._font_data,
                text_scale = self._text_scale
            ))
