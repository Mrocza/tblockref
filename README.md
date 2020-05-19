***

`ref = tblockref.reference(scale = 2, margin = 6)`
-----
This is the class constructor. It allows setting up base properties of the reference chart.      
**scale**     
Sets the amout of pixels representing one pixel on a sprite.
The default value is 2. One pixel in a sprite is two screen-pixels wide (just like in the game).     
**margin**     
Sets the amout of white space at the edges of the chart expressed in pixels.
Default value is 6.

`ref.column(width = int)`     
-----
Resets block position back to the top and creates a new column in the chart.     
**width**     
Specifies the width of the new column. Values too small will result in overlap between columns.

`ref.block(block_name = '')`     
-----
Places a block in the chart, its sprite and name. If no local resource for the sprite is found attempts to download off the wiki.     
**block_name**     
Specifies the name of the block to be placed. When name in an empty string or no name is provided a break in the column is created instead (see `ref.space()`)

`ref.space()`     
-----
Creates a break in the current column leaving empty space.

`ref.update_all()`     
-----
Updates all locally stored sprites by redownloading from the wiki.
TODO: Add a hash check and skip downloading files that are already up to date.

`ref.embed()`     
-----
Embeds all currently included block sprites into the svg file.

`ref.text_to_symbols()`     
-----
TODO: Write a function that converts glyphs to SVG symbols and converts text to <use> elements.

`ref.out(file_name='output.svg')`     
-----
Save the reference to a file.     
**file_name**     
Specifies the path to file and filename.

