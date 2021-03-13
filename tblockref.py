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

        self._block_dict = {}
        self._height = 0
        self._width = 0
        self._column_width = 0

        # First slot in the reference starts off of the margin values.
        self._pos_x = self._margin
        self._pos_y = self._margin

    def block(self, block_name = None, file_name = None):
        """
        Places a block into the reference in current position and advances to
        the next slot.
        """
        if not block_name:
            # If block name is not specified advances two slots forward creating
            # a gap in the current column. One slot is 12px wide.
            self._pos_y += 24*self._scale
            return

        print(f'Adding block {block_name} ...')

        if not file_name:
            # If the filename is not specified a guess is made based on block
            # name with both png and gif extentions tested.
            file_name = block_name.replace(' ','_') + '_(placed)'
            for format in ['.png', '.gif']:
                if os.path.isfile('res/' + file_name + format):
                    file_name += format
                    self._getfile(file_name)
                    break
                if self._isfile(file_name + format):
                    file_name += format
                    self._getfile(file_name)
                    break
        else:
            # If filename is provided all checks are skipped.
            self._getfile(file_name)

        # Setting data for current block
        self._block_dict[block_name] = {
            'sprite_x': str(self._pos_x),
            'sprite_y': str(self._pos_y),
            'sprite_width': str(24*self._scale),
            'sprite_height': str(24*self._scale),
            'sprite_href': 'res/'+file_name,
            'text_x': self._pos_x+30*self._scale,
            'text_y': self._pos_y+12*self._scale,
            'text_tspan': block_name,
            # List of unicode codes for each character in tspan.
            # This is neccessary for font handling later.
            'text_tspan_unicode_list': [str(ord(char)) for char in block_name]
        }

        # Advancing to next slot position. One slot is 12px wide.
        self._pos_y += 12*self._scale

        # Adjusting document height to the highest y value reached.
        if self._height < self._pos_y + 12*self._scale:
            self._height = self._pos_y + 12*self._scale

    def column(self, column_width):
        """
        Creates a new column in the chart.
        The width of the column has to be specified as a pixel value.

        Column width can be calculated automatically based on
        'text_tspan_unicode_list' and 'horiz-adv-x' in font data.
        I haven't gotten to automating that part yet. That's a TODO.
        """
        self._pos_y = self._margin # reset y value back to top
        self._pos_x += self._column_width # adjust x value by previous column
        self._column_width = column_width # set current column width
        self._width += column_width # increase document width to fit new column

    def _isfile(self, file_name):
        """
        Checks if the file is present on the wiki.

        This can be integrated into _getfile for a single function that checks
        for availibility and downloads if true. That would cut on complexity.
        I haven't gotten there yet.
        """
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
        """
        Gets a direct image link from the wiki and downloads that image if the
        modification date is newer than for the locally stored resource.
        """
        # Retrieving a direct image url.
        response = urllib.request.urlopen(
            'https://terraria.gamepedia.com/File:'+file_name)
        soup = BeautifulSoup(response.read(), 'html.parser')
        image_href = soup.find("div", {"class": "fullMedia"}).a['href']
        # Getting last modification timestamp from the url parameter 'cb'.
        parsed = urllib.parse.urlparse(image_href)
        mod_date_string = (urllib.parse.parse_qs(parsed.query)['cb'])[0]
        mod_date = datetime.strptime(mod_date_string, '%Y%m%d%H%M%S')
        # Getting last modification timestamp for local file.
        if os.path.isfile('res/'+file_name):
            last_update = datetime.fromtimestamp(
                os.path.getmtime('res/'+file_name))
        else:
            last_update = datetime(1970,1,1)
        # Downloading if newer.
        if mod_date > last_update:
            urllib.request.urlretrieve(image_href, 'res/'+file_name)

    def out(self, output):
        """
        Outputs a completed reference to a specified file.
        """
        # Embedding all images into the file.
        for block in self._block_dict:
            with open(self._block_dict[block]['sprite_href'], "rb") as f:
                self._block_dict[block]['sprite_href'] = (
                    f'data:image/{os.path.splitext(self._block_dict[block]["sprite_href"])[1][1:]};base64,'
                    + base64.b64encode(f.read()).decode())

        # Loading font information and template.
        with open('font_data.json', 'r') as f:
            font_data = json.load(f)
        with open('svg_template.svg.jinja', 'r') as f:
            svg = Template(f.read(), trim_blocks=True, lstrip_blocks=True)
        # Rendering template and writing to file.
        with open(output, 'w') as f:
            f.write(svg.render(
                svg_width = self._width + self._margin,
                svg_height = self._height + self._margin,
                block_values = self._block_dict.values(),
                svg_glyphs = font_data,
                # Nominally the svg font used here is about 1024pt in size.
                # Scale listed below brings it to about 12pt.
                text_scale = 0.01172,
                # The text in its raw state seems shifted a bit down and right.
                # Offset is introduced to align it with the sprites.
                text_offset_x = -5,
                text_offset_y = -3
            ))
