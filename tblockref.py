import os
import re
import urllib.request

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

  def block(self, block_name = '', file_name = ''):
    if block_name == '':
      self.space()
      return

    if file_name == '':
      file_name = block_name.replace(' ','_')+'_(placed)'

      if os.path.isfile('res/'+file_name+'.png'):
        file_name += '.png'
      elif os.path.isfile('res/'+file_name+'.gif'):
        file_name += '.gif'
      else:
        try:
          response = urllib.request.urlopen('https://terraria.gamepedia.com/File:'+file_name+'.png')
          file_name += '.png'
        except:
          try:
            response = urllib.request.urlopen('https://terraria.gamepedia.com/File:'+file_name+'.gif')
            file_name += '.gif'
          except:
              raise FileNotFoundError(block_name+' does not exist on the wiki under expected file name')
        html = response.read()
        image_html = re.search('<div class="fullMedia"><p><a href="(.*)\?version',html.decode("utf-8")).group(1)
        urllib.request.urlretrieve(image_html, 'res/'+file_name)

    else:
        response = urllib.request.urlopen('https://terraria.gamepedia.com/File:'+file_name)
        html = response.read()
        image_html = re.search('<div class="fullMedia"><p><a href="(.*)\?version',html.decode("utf-8")).group(1)
        urllib.request.urlretrieve(image_html, 'res/'+file_name)

    self.__block_dict[block_name] = {'sprite_x':str(self.__pos_x),
                                   'sprite_y':str(self.__pos_y),
                                   'sprite_width':str(24*self.__scale),
                                   'sprite_height':str(24*self.__scale),
                                   'sprite_href':'res/'+file_name,
                                   'text_x':str(self.__pos_x+30*self.__scale),
                                   'text_y':str(self.__pos_y+12*self.__scale),
                                   'text_tspan':block_name}

    self.__pos_y += 12*self.__scale

    #adjust document height to the highest y value reached
    if self.__height < self.__pos_y + 12*self.__scale:
      self.__height = self.__pos_y + 12*self.__scale

  def space(self):
    self.__pos_y += 24*self.__scale

  def column(self, column_width):
    self.__pos_y = self.__margin #reset y value back to top
    self.__pos_x += self.__column_width #adjust x value by previous column width
    self.__column_width = column_width #set current column width
    self.__width += column_width

  def update_all(self):
    i=0
    list_of_files = os.listdir('res/')

    for file in list_of_files:
      i+=1
      print('{0}/{1} updating {2}...'.format(i, len(list_of_files), file))

      response = urllib.request.urlopen('https://terraria.gamepedia.com/File:'+file)
      html = response.read()
      image_html = re.search('<div class="fullMedia"><p><a href="(.*)\?version',html.decode("utf-8")).group(1)
      urllib.request.urlretrieve(image_html, 'res/'+file)

  def embed(self):
    import base64
    for block in self.__block_dict:
      with open(self.__block_dict[block]['sprite_href'], "rb") as f:
        self.__block_dict[block]['sprite_href'] = 'data:image/png;base64,'+base64.b64encode(f.read()).decode()

  def out(self, output):
    width = self.__width+self.__margin
    height = self.__height+self.__margin

    f = open(output,'w')
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write(('<svg width="{0}"'
             ' height="{1}"'
             ' xmlns="http://www.w3.org/2000/svg"'
             ' xmlns:xlink="http://www.w3.org/1999/xlink">\n'
             ).format(width, height))
    f.write(('  <rect width="{0}"'
             ' height="{1}"'
             ' fill="#fff"/>\n'
             ).format(width, height))
    f.write('  <g>\n')
    for d in self.__block_dict.values():
      f.write(('    <image x="{sprite_x}"'
               ' y="{sprite_y}"'
               ' width="{sprite_width}"'
               ' height="{sprite_height}"'
               ' image-rendering="optimizeSpeed"'
               ' xlink:href="{sprite_href}"/>\n'
               ).format_map(d))
    f.write('  </g>\n')
    f.write(('  <g fill="#000000"'
             ' font-family="Andy"'
             ' font-size="{0}px">\n'
             ).format(12*self.__scale))
    for d in self.__block_dict.values():
      f.write(('    <text x="{text_x}" y="{text_y}">'
               '<tspan>{text_tspan}</tspan></text>'
               ).format_map(d))
    f.write('  </g>\n')
    f.write('</svg>\n')
    f.close()
