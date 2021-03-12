***
```
from tblockref import Reference
ref = Reference(scale = 2, margin = 6)
```
-----
This is the class constructor. It allows setting up base properties of the reference chart.      
**scale**     
Sets the amount of pixels representing one pixel on a sprite.
The default value is 2. One pixel in a sprite is two screen-pixels wide (just like in the game).     
**margin**     
Sets the amount of white space at the edges of the chart expressed in pixels.
Default value is 6.

`ref.column(width = int)`     
-----
Resets block position back to the top and creates a new column in the chart.     
**width**     
Specifies the width of the new column. Values too small will result in overlap between columns.

`ref.block(block_name = None, file_name = None)`     
-----
Places a block in the chart, its sprite and name. Checks the modification date on existing local files. If no local resource for the sprite is found attempts to download off the wiki.     
**block_name**     
Specifies the name of the block to be placed. When name in an empty string or no name is provided a break in the column is created instead (see `ref.space()`)     
**file_name**     
Specifies the name of the sprite image on the wiki. If no name is provided a guess is made based on block name.

`ref.space()`     
-----
Creates a break in the current column leaving empty space.

`ref.embed()`     
-----
Embeds all currently included block sprites into the svg file.

`ref.out(file_name='output.svg')`     
-----
Save the reference to a file.
**file_name**     
Specifies the path to file and filename.
