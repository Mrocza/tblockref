import os
from PIL import Image
import subprocess

def iswall(block_name):
    for i in ['Wall', 'Stained', 'Fence', 'Sail']:
        if i in block_name: return True
    return False

for file in os.listdir('res/'):
    if os.path.splitext(file)[1] == '.gif':
        continue

    if iswall(file):
        size = (32,32)
    else:
        size = (24,24)
    img = Image.open('res/'+file)
    img = img.convert(mode='P', palette=Image.ADAPTIVE)
    img = img.resize(size, resample=Image.NEAREST)
    img.save('res/'+file, "PNG")
    subprocess.run('pngout.exe '+'res/'+file)
