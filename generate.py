from tblockref import reference

#numbers denote width of new column
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
Bone Block
Pumpkin
Hay
Glowing Mushroom
Cactus
Coralstone Block
Cog
Asphalt Block
Crystal Block
Martian Conduit Plating
Bubble
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
Amethyst
Topaz
Sapphire
Emerald
Ruby
Diamond

Gray Brick
Stone Slab
Sandstone Brick
Sandstone Slab
Red Brick
Iridescent Brick
Mudstone Brick
Ebonstone Brick
Pearlstone Brick
Snow Brick
Ice Brick
Sunplate Block
Rainbow Brick
Pink Brick
Green Brick
Blue Brick
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

Active Stone Block
Inactive Stone Block
Conveyor Belt (Clockwise)
Conveyor Belt (Counter Clockwise)"""

blocklist = blocklist.split('\n')

r = reference()

for i in blocklist:
  if i.isnumeric():
    r.column(int(i))
  elif i == '':
    r.space()
  else:
    r.block(i)

r.embed()
r.out('output.svg')
