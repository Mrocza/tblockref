from tblockref import Reference

# numbers denote width of new column
# blocks with filenames that do not match the blockname
# need filename specified after ' > '
blocklist = """310
Dirt Block
Grass Block
Corrupt Grass Block
Crimson Grass Block
Hallowed Grass Block
Mud Block
Jungle Grass Block
Mushroom Grass Block
Clay Block
Ash Block
Silt Block

Sand Block
Hardened Sand Block
Sandstone Block
Smooth Sandstone
Ebonsand Block
Hardened Ebonsand Block
Ebonsandstone Block
Crimsand Block
Hardened Crimsand Block
Crimsandstone Block
Pearlsand Block
Hardened Pearlsand Block
Pearlsandstone Block
Desert Fossil
Sturdy Fossil

Snow Block
Slush Block
Ice Block
Purple Ice Block
Red Ice Block
Pink Ice Block
Thin Ice
Magical Ice Block

Wood
Ebonwood
Shadewood
Pearlwood
Boreal Wood
Rich Mahogany
Palm Wood
Dynasty Wood
Spooky Wood
Living Wood
Leaf Block
Living Mahogany
Mahogany Leaf Block
Bamboo
Large Bamboo

Honey Block
Crispy Honey Block
Hive
Candy Cane Block
Green Candy Cane Block
Pine Tree Block
Cloud
Rain Cloud
Snow Cloud
Flesh Block
Lesion Block
Bone Block
Pumpkin
Hay
Glowing Mushroom
Cactus
Coralstone Block
Shell Pile
Cog
Asphalt Block
Crystal Block
Martian Conduit Plating
Echo Block
Anti-Portal Block
Bubble
Grate
Living Fire Block
Living Demon Fire Block
Living Frost Fire Block
Living Cursed Fire Block
Living Ichor Block
Living Ultrabright Fire Block
Smoke Block
290
Stone Block
Ebonstone Block
Crimstone Block
Pearlstone Block
Marble Block
Smooth Marble Block
Granite Block
Smooth Granite Block
Blue Moss Block
Red Moss Block
Chartreuse Moss Block
Teal Moss Block
Purple Moss Block
Fire Moss Block
Amethyst Stone Block > Amethyst_(placed).png
Topaz Stone Block > Topaz_(placed).png
Sapphire Stone Block > Sapphire_(placed).png
Emerald Stone Block > Emerald_(placed).png
Ruby Stone Block > Ruby_(placed).png
Diamond Stone Block > Diamond_(placed).png

Gray Brick
Stone Slab
Sandstone Brick
Sandstone Slab
Red Brick
Iridescent Brick
Mudstone Brick
Ebonstone Brick
Crimstone Brick
Pearlstone Brick
Snow Brick
Ice Brick
Sunplate Block
Rainbow Brick
Pink Brick
Cracked Pink Brick
Green Brick
Cracked Green Brick
Blue Brick
Cracked Blue Brick
Lihzahrd Brick

Gray Stucco
Red Stucco
Yellow Stucco
Green Stucco
Red Dynasty Shingles
Blue Dynasty Shingles

Glass
Confetti Block
Midnight Confetti Block
Waterfall Block
Honeyfall Block
Lavafall Block
Sandfall Block
Snowfall Block
Blue Starry Block
Gold Starry Block

White Team Block
Red Team Block
Green Team Block
Blue Team Block
Pink Team Block
Yellow Team Block

Silly Pink Balloon
Silly Green Balloon
Silly Purple Balloon

Spike
Wooden Spike

Cobweb
390
Copper Ore
Tin Ore
Iron Ore
Lead Ore
Silver Ore
Tungsten Ore
Gold Ore
Platinum Ore
Meteorite
Demonite Ore
Crimtane Ore
Obsidian
Hellstone
Cobalt Ore
Palladium Ore
Mythril Ore
Orichalcum Ore
Adamantite Ore
Titanium Ore
Chlorophyte Ore
Luminite

Copper Brick
Copper Plating
Tin Brick
Tin Plating
Iron Brick
Lead Brick
Silver Brick
Tungsten Brick
Gold Brick
Platinum Brick
Meteorite Brick
Demonite Brick
Crimtane Brick
Obsidian Brick
Hellstone Brick
Cobalt Brick
Palladium Column
Mythril Brick
Bubblegum Block
Adamantite Beam
Titanstone Block
Chlorophyte Brick
Shroomite Plating
Luminite Brick
Nebula Brick
Solar Brick
Stardust Brick
Vortex Brick

Nebula Fragment Block
Solar Fragment Block
Stardust Fragment Block
Vortex Fragment Block

Amethyst Gemspark Block
Topaz Gemspark Block
Sapphire Gemspark Block
Emerald Gemspark Block
Ruby Gemspark Block
Diamond Gemspark Block
Amber Gemspark Block

Offline Amethyst Gemspark Block
Offline Topaz Gemspark Block
Offline Sapphire Gemspark Block
Offline Emerald Gemspark Block
Offline Ruby Gemspark Block
Offline Diamond Gemspark Block
Offline Amber Gemspark Block

Slime Block
Pink Slime Block
Frozen Slime Block

Active Stone Block > Stone_Block_(placed).png
Inactive Stone Block
Conveyor Belt (Clockwise)
Conveyor Belt (Counter Clockwise)"""

blocklist = blocklist.split('\n')

r = Reference()

for i in blocklist:
  if i.isnumeric():
    r.column(int(i))
  else:
    if i.find(' > ') == -1:
        r.block(i)
    else:
        j = i.split(' > ')
        r.block(j[0],j[1])

r.embed()
r.out('output.svg')
