import os
import re
import base64
import urllib.request, urllib.error
from jinja2 import Template
from bs4 import BeautifulSoup

class reference:
    def __init__(self, scale = 2, margin = 6):
        self.__margin = margin
        self.__scale = scale

        self.__block_dict = {}
        self.__height = 0
        self.__width = 0
        self.__column_width = 0

        self.__pos_x = self.__margin
        self.__pos_y = self.__margin

    def block(self, block_name = None, file_name = None):
        if not block_name:
            self.space()
            return

        if not file_name:
            file_name = block_name.replace(' ','_')+'_(placed)'
            for format in ['.png', '.gif']:
                if os.path.isfile('res/'+file_name+format):
                    file_name += format
                    break
                if self.__isfile(file_name+format):
                    file_name += format
                    self.__getfile(file_name)
                    break
        else:
            if not os.path.isfile('res/'+file_name):
                __getfile(filename)

        # set data for current block
        self.__block_dict[block_name] = {
            'sprite_x': str(self.__pos_x),
            'sprite_y': str(self.__pos_y),
            'sprite_width': str(24*self.__scale),
            'sprite_height': str(24*self.__scale),
            'sprite_href': 'res/'+file_name,
            'text_x': str(self.__pos_x+30*self.__scale),
            'text_y': str(self.__pos_y+12*self.__scale),
            'text_tspan': block_name
        }

        # advance to next block posiotion
        self.__pos_y += 12*self.__scale

        # adjust document height to the highest y value reached
        if self.__height < self.__pos_y + 12*self.__scale:
            self.__height = self.__pos_y + 12*self.__scale

    def space(self):
        self.__pos_y += 24*self.__scale

    def column(self, column_width):
        self.__pos_y = self.__margin # reset y value back to top
        self.__pos_x += self.__column_width # adjust x value by previous column width
        self.__column_width = column_width # set current column width
        self.__width += column_width # increase document width to fit new column

    def __isfile(self, file_name):
        try:
            urllib.request.urlopen('https://terraria.gamepedia.com/File:'+file_name)
        except urllib.error.HTTPError as e:
            # Return code error (e.g. 404, 501, ...)
            print(f'HTTPError: {e.code}')
            return False
        except urllib.error.URLError as e:
            # Not an HTTP-specific error (e.g. connection refused)
            print(f'URLError: {e.reason}')
            return False
        else:
            return True

    def __getfile(self, file_name):
        response = urllib.request.urlopen('https://terraria.gamepedia.com/File:'+file_name)
        soup = BeautifulSoup(response.read(), 'html.parser')
        image_href = soup.find("div", {"class": "fullMedia"}).a['href']
        urllib.request.urlretrieve(image_href, 'res/'+file_name)

    def update_all(self):
        list_of_files = os.listdir('res/')

        for i, file in enumerate(list_of_files, start=1):
            print(f'{i}/{len(list_of_files)} updating {file}...')
            self.__getfile(file)

    def embed(self):
        for block in self.__block_dict:
            with open(self.__block_dict[block]['sprite_href'], "rb") as f:
                self.__block_dict[block]['sprite_href'] = 'data:image/png;base64,'+base64.b64encode(f.read()).decode()

    def out(self, output):
        with open('svg_template.svg', 'r') as f:
            svg = Template(f.read(), trim_blocks=True, lstrip_blocks=True)
        with open(output, 'w') as f:
            f.write(svg.render(
                svg_width= self.__width + self.__margin,
                svg_height= self.__height + self.__margin,
                block_values= self.__block_dict.values()
            ))
