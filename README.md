***
List of blocks for the reference image can be found in `generate.py`.

tblockref.py
-------
```
from tblockref import Reference
ref = Reference(scale = 2, margin = 6)
```
This is the class constructor. It allows setting up base properties of the reference chart.      
**scale**     
Sets the amount of pixels representing one pixel on a sprite.
The default value is 2. One pixel in a sprite is two screen-pixels wide (just like in the game).     
**margin**     
Sets the amount of white space in pixels at the edges of the chart and between columns.
Default value is 6.

`ref.block(block_name = None, file_name = None)`     
Places a block in the chart, its sprite and name. Checks the modification date on existing local files and download a sprite if a new version is available (or if there is no local resource for the sprite).     
**block_name**     
Specifies the name of the block to be placed. When name in an empty string or no name is provided a break in the column is created instead.    
**file_name**     
Specifies the name of the sprite image on the wiki. If no name is provided a guess is made based on block name.

`ref.column()`     
Closes current column in the chart and resets block position back to the top.     

`ref.out(file_name='output.svg')`     
Save the reference to a file.     
**file_name**     
Specifies the path to file and filename.
