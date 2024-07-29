import os
import json
import base64
import urllib.error
import urllib.request
from jinja2 import Template
from bs4 import BeautifulSoup
from datetime import datetime

class Reference:
    def __init__(self, scale = 2, margin = 6, unicode = False):
        self._margin = margin
        self._scale = scale
        self.unicode = unicode
        # Nominally the svg font used here is about 1024pt in size.
        # Number listed below brings it down to about 12pt (with scale = 2).
        self._text_scale = 0.00586 * scale

        self._block_dict = dict()
        self._height = int()
        self._width = int()
        self._column_id = 0

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
            file_name = block_name.replace(' ','_') + '_(placed)'
            for format in ['', '.png', '.gif']:
                if os.path.isfile('res/' + file_name + format):
                    file_name += format

        # List of unicode codes for each character in blockname.
        # This is neccessary for font handling.
        unicode_list = [str(ord(char)) for char in block_name]

        # Setting data for current block
        self._block_dict[block_name] = {
            'sprite_href': 'res/'+file_name,
            'column_id': self._column_id,
            'sprite_x': self._pos_x,
            'sprite_y': self._pos_y,
            # Sprites have a nominal resolution of 24x24 px.
            'sprite_width': 24 * self._scale,
            'sprite_height': 24 * self._scale,
            # text is shifted 27px right and 11px down from sprite position
            'text_x': self._pos_x + 27*self._scale,
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
            self._block_dict[block_name]['text_x'] += 3 * self._scale
            self._block_dict[block_name]['text_y'] -= 3 * self._scale

        # Advancing to next slot position. One slot is 12px wide.
        self._pos_y += 12 * self._scale

        # Adjusting document height to the highest y value reached.
        if self._height < self._pos_y + 12*self._scale:
            self._height = self._pos_y + 12*self._scale

    def column(self):
        """
        Creates a new column in the chart.
        """
        # Resetting y value back to top.
        self._pos_y = self._margin
        # Filtering data to current column
        data = [v for v in self._block_dict.values()
                if v['column_id'] == self._column_id]
        # Checking max name width in the column and advancing position.
        max_name_width = max([v['text_tspan_width'] for v in data])
        max_sprite_width = max([v['sprite_width'] for v in data])
        self._pos_x += max_name_width + max_sprite_width + self._margin

        # Increasing document width to fit new column.
        self._width = self._pos_x
        # Advancing column id
        self._column_id += 1

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
