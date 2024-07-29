import urllib.error
import urllib.request
from bs4 import BeautifulSoup
from tblockref import Reference

code = '''Dirt Block
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
Ash Wood
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
Poo
Bone Block
Pumpkin
Hay
Glowing Mushroom
Cactus
Coralstone Block
Reef Block
Shell Pile
Cog
Asphalt Block
Crystal Block
Aetherium Block
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

Cobweb
Spider Nest Block



Stone Block
Ebonstone Block
Crimstone Block
Pearlstone Block
Marble Block
Smooth Marble Block
Granite Block
Smooth Granite Block

Amethyst Stone Block > Amethyst_(placed).png
Topaz Stone Block > Topaz_(placed).png
Sapphire Stone Block > Sapphire_(placed).png
Emerald Stone Block > Emerald_(placed).png
Ruby Stone Block > Ruby_(placed).png
Diamond Stone Block > Diamond_(placed).png

Green Moss > Teal_Moss_Block_(placed).png
Brown Moss > Chartreuse_Moss_Block_(placed).png
Red Moss > Red_Moss_Block_(placed).png
Blue Moss > Blue_Moss_Block_(placed).png
Purple Moss > Purple_Moss_Block_(placed).png
Lava Moss > Fire_Moss_Block_(placed).png
Lava Moss Brick
Krypton Moss > Krypton_Moss_Block_(placed).png
Krypton Moss Brick
Xenon Moss > Xenon_Moss_Block_(placed).png
Xenon Moss Brick
Argon Moss > Argon_Moss_Block_(placed).png
Argon Moss Brick
Neon Moss Brick
Helium Moss Brick

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
Aetherium Brick
Sunplate Block
Rainbow Brick
Pink Brick
Cracked Pink Brick
Ancient Pink Brick
Green Brick
Cracked Green Brick
Ancient Green Brick
Blue Brick
Cracked Blue Brick
Ancient Blue Brick
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

Slime Block
Pink Slime Block
Frozen Slime Block



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
Ancient Copper Brick
Copper Plating
Tin Brick
Tin Plating
Iron Brick
Lead Brick
Silver Brick
Ancient Silver Brick
Tungsten Brick
Gold Brick
Ancient Gold Brick
Platinum Brick
Meteorite Brick
Demonite Brick
Crimtane Brick
Obsidian Brick
Ancient Obsidian Brick
Hellstone Brick
Ancient Hellstone Brick
Cobalt Brick
Ancient Cobalt Brick
Palladium Column
Mythril Brick
Ancient Mythril Brick
Bubblegum Block
Adamantite Beam
Titanstone Block
Chlorophyte Brick
Shroomite Plating
Nebula Brick
Solar Brick
Stardust Brick
Vortex Brick
Luminite Brick
Astra Brick
Cosmic Ember Brick
Cryocore Brick
Dark Celestial Brick
Heavenforge Brick
Lunar Rust Brick
Mercury Brick
Star Royale Brick

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

Active Stone Block > Stone_Block_(placed).png
Inactive Stone Block
Conveyor Belt (Clockwise)
Conveyor Belt (Counter Clockwise)

Spike
Wooden Spike'''


ref = Reference(margin = 10)
blocklist = code.strip('\n')
for column in blocklist.split('\n\n\n'):
    column = column.strip('\n')
    for line in column.split('\n'):
        ref.block(*line.split(' > '))
    ref.column()
ref.out(f'output-en.svg')
