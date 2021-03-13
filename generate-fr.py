from tblockref import Reference

# numbers denote width of new column
# blocks with filenames that do not match the blockname
# need filename specified after ' > '
blocklist = """330
Bloc de terre > Dirt_Block_(placed).png
Bloc d'herbe > Grass_Block_(placed).png
Bloc d'herbe corrompue > Corrupt_Grass_Block_(placed).png
Bloc d'herbe carmin > Crimson_Grass_Block_(placed).png
Bloc d'herbe sacrée > Hallowed_Grass_Block_(placed).png
Bloc de boue > Mud_Block_(placed).png
Bloc d'herbe de la jungle > Jungle_Grass_Block_(placed).png
Bloc d'herbe de champignon > Mushroom_Grass_Block_(placed).png
Bloc d'argile > Clay_Block_(placed).png
Bloc de cendre > Ash_Block_(placed).png
Bloc de vase > Silt_Block_(placed).png

Bloc de sable > Sand_Block_(placed).png
Bloc de sable durci > Hardened_Sand_Block_(placed).png
Bloc de grès > Sandstone_Block_(placed).png
Grès lisse > Smooth_Sandstone_(placed).png
Bloc de sable d'ébène > Ebonsand_Block_(placed).png
Bloc de sable d'ébène durci > Hardened_Ebonsand_Block_(placed).png
Bloc de grès d'ébène > Ebonsandstone_Block_(placed).png
Bloc de sable carmin > Crimsand_Block_(placed).png
Bloc de sable carmin durci > Hardened_Crimsand_Block_(placed).png
Bloc de grès carmin > Crimsandstone_Block_(placed).png
Bloc de sable perlé > Pearlsand_Block_(placed).png
Bloc de sable perlé durci > Hardened_Pearlsand_Block_(placed).png
Bloc de grès perlé > Pearlsandstone_Block_(placed).png
Fossile du désert > Desert_Fossil_(placed).png
Fossile solide > Sturdy_Fossil_(placed).png

Bloc de neige > Snow_Block_(placed).png
Bloc de gadoue > Slush_Block_(placed).png
Bloc de glace > Ice_Block_(placed).png
Bloc de glace violet > Purple_Ice_Block_(placed).png
Bloc de glace rouge > Red_Ice_Block_(placed).png
Bloc de glace rose > Pink_Ice_Block_(placed).png
Glace fine > Thin_Ice_(placed).png
Bloc de glace magique > Magical_Ice_Block_(placed).png

Bois > Wood_(placed).png
Ébène > Ebonwood_(placed).png
Bois d'ombre > Shadewood_(placed).png
Bois perlé > Pearlwood_(placed).png
Bois boréal > Boreal_Wood_(placed).png
Acajou riche > Rich_Mahogany_(placed).png
Palmier > Palm_Wood_(placed).png
Bois de dynastie > Dynasty_Wood_(placed).png
Bois sinistre > Spooky_Wood_(placed).png
Bois vivant > Living_Wood_(placed).png
Bloc de feuille > Leaf_Block_(placed).png
Acajou riche vivant > Living_Mahogany_(placed).png
Bloc de feuilles d'acajou riche > Mahogany_Leaf_Block_(placed).png
Bambou > Bamboo_(placed).png
Bambou épais > Large_Bamboo_(placed).png

Bloc de miel > Honey_Block_(placed).png
Bloc de miel croquant > Crispy_Honey_Block_(placed).png
Ruche > Hive_(placed).png
Bloc de sucre d'orge > Candy_Cane_Block_(placed).png
Bloc de sucre d'orge vert > Green_Candy_Cane_Block_(placed).png
Bloc de sapin > Pine_Tree_Block_(placed).png
Nuage > Cloud_(placed).png
Nuage de pluie > Rain_Cloud_(placed).png
Nuage de neige > Snow_Cloud_(placed).png
Bloc de chair > Flesh_Block_(placed).png
Bloc de plaie > Lesion_Block_(placed).png
Bloc d'os > Bone_Block_(placed).png
Citrouille > Pumpkin_(placed).png
Foin > Hay_(placed).png
Champignon luisant > Glowing_Mushroom_(placed).png
Cactus > Cactus_(placed).png
Bloc de corail > Coralstone_Block_(placed).png
Tas de coquillages > Shell_Pile_(placed).png
Roue dentée > Cog_(placed).gif
Bloc d'asphalte > Asphalt_Block_(placed).png
Bloc de cristal > Crystal_Block_(placed).png
Plaque de conduit martienne > Martian_Conduit_Plating_(placed).png
Bloc Echo > Echo_Block_(placed).png
Bloc anti-portail > Anti-Portal_Block_(placed).png
Bulle > Bubble_(placed).gif
Grille > Grate_(placed).png
Bloc de feu vivant > Living_Fire_Block_(placed).gif
Bloc de feu démoniaque vivant > Living_Demon_Fire_Block_(placed).gif
Bloc de feu givré vivant > Living_Frost_Fire_Block_(placed).gif
Bloc de feu maudit vivant > Living_Cursed_Fire_Block_(placed).gif
Bloc d'ichor vivant > Living_Ichor_Block_(placed).gif
Bloc de feu intense vivant > Living_Ultrabright_Fire_Block_(placed).gif
Bloc de fumée > Smoke_Block_(placed).gif
300
Bloc de pierre > Stone_Block_(placed).png
Bloc de pierre d'ébène > Ebonstone_Block_(placed).png
Bloc de pierre carmin > Crimstone_Block_(placed).png
Bloc de pierre perlée > Pearlstone_Block_(placed).png
Bloc de marbre > Marble_Block_(placed).png
Bloc de marbre lisse > Smooth_Marble_Block_(placed).png
Bloc de granite > Granite_Block_(placed).png
Bloc de granite lisse > Smooth_Granite_Block_(placed).png
Mousse bleue > Blue_Moss_Block_(placed).png
Mousse rouge > Red_Moss_Block_(placed).png
Mousse marron > Chartreuse_Moss_Block_(placed).png
Mousson verte > Teal_Moss_Block_(placed).png
Mousse violette > Purple_Moss_Block_(placed).png
Mousse de lave > Fire_Moss_Block_(placed).png
Mousse de krypton > Krypton_Moss_Block_(placed).png
Mousse de xénon > Xenon_Moss_Block_(placed).png
Mousse d'argon > Argon_Moss_Block_(placed).png
Bloc de pierre améthyste > Amethyst_(placed).png
Bloc de topaze > Topaz_(placed).png
Bloc de saphir > Sapphire_(placed).png
Bloc d'émeraude > Emerald_(placed).png
Bloc de rubis > Ruby_(placed).png
Bloc de diamant > Diamond_(placed).png

Brique grise > Gray_Brick_(placed).png
Dalle de pierre > Stone_Slab_(placed).png
Brique de grès > Sandstone_Brick_(placed).png
Dalle de grès > Sandstone_Slab_(placed).png
Brique rouge > Red_Brick_(placed).png
Brique irisée > Iridescent_Brick_(placed).png
Brique de pierre boueuse > Mudstone_Brick_(placed).png
Brique de pierre d'ébène > Ebonstone_Brick_(placed).png
Brique de pierre carmin > Crimstone_Brick_(placed).png
Brique de pierre perlée > Pearlstone_Brick_(placed).png
Brique de neige > Snow_Brick_(placed).png
Brique de glace > Ice_Brick_(placed).png
Bloc de soleil > Sunplate_Block_(placed).png
Brique arc-en-ciel > Rainbow_Brick_(placed).gif
Brique rose > Pink_Brick_(placed).png
Brique rose fissurée > Cracked_Pink_Brick_(placed).png
Brique verte > Green_Brick_(placed).png
Brique verte fissurée > Cracked_Green_Brick_(placed).png
Brique bleue > Blue_Brick_(placed).png
Brique bleue fissurée > Cracked_Blue_Brick_(placed).png
Brique de lihzahrd > Lihzahrd_Brick_(placed).png

Stuc gris > Gray_Stucco_(placed).png
Stuc rouge > Red_Stucco_(placed).png
Stuc jaune > Yellow_Stucco_(placed).png
Stuc vert > Green_Stucco_(placed).png
Galets de dynastie rouge > Red_Dynasty_Shingles_(placed).png
Galets de dynastie bleue > Blue_Dynasty_Shingles_(placed).png

Verre > Glass_(placed).png
Bloc de confetti > Confetti_Block_(placed).gif
Bloc de confetti de minuit > Midnight_Confetti_Block_(placed).gif
Bloc de chute d'eau > Waterfall_Block_(placed).gif
Bloc de chute de miel > Honeyfall_Block_(placed).gif
Bloc de chute de lave > Lavafall_Block_(placed).gif
Bloc de chute de sable > Sandfall_Block_(placed).gif
Bloc de chute de neige > Snowfall_Block_(placed).gif
Bloc étoilé bleu > Blue_Starry_Block_(placed).gif
Bloc étoilé or > Gold_Starry_Block_(placed).gif

Bloc de l'équipe blanche > White_Team_Block_(placed).png
Bloc de l'équipe rouge > Red_Team_Block_(placed).png
Bloc de l'équipe verte > Green_Team_Block_(placed).png
Bloc de l'équipe bleue > Blue_Team_Block_(placed).png
Bloc de l'équipe rose > Pink_Team_Block_(placed).png
Bloc de l'équipe jaune > Yellow_Team_Block_(placed).png

Ballon loufoque rose > Silly_Pink_Balloon_(placed).png
Ballon loufoque vert > Silly_Green_Balloon_(placed).png
Ballon loufoque violet > Silly_Purple_Balloon_(placed).png

Pointe > Spike_(placed).png
Pointe en bois > Wooden_Spike_(placed).png

Toile d'araignée > Cobweb_(placed).png
390
Minerai de cuivre > Copper_Ore_(placed).png
Minerai d'étain > Tin_Ore_(placed).png
Minerai de fer > Iron_Ore_(placed).png
Minerai de plomb > Lead_Ore_(placed).png
Minerai d'argent > Silver_Ore_(placed).png
Minerai de tungstène > Tungsten_Ore_(placed).png
Minerai d'or > Gold_Ore_(placed).png
Minerai de platine > Platinum_Ore_(placed).png
Météorite > Meteorite_(placed).png
Minerai de démonite > Demonite_Ore_(placed).png
Minerai de carmitane > Crimtane_Ore_(placed).png
Obsidienne > Obsidian_(placed).png
Pierre infernale > Hellstone_(placed).png
Minerai de cobalt > Cobalt_Ore_(placed).png
Minerai de palladium > Palladium_Ore_(placed).png
Minerai de mithril > Mythril_Ore_(placed).png
Minerai d'orichalque > Orichalcum_Ore_(placed).png
Minerai d'adamantite > Adamantite_Ore_(placed).png
Minerai de titane > Titanium_Ore_(placed).png
Minerai de chlorophyte > Chlorophyte_Ore_(placed).png
Luminite > Luminite_(placed).png

Brique en cuivre > Copper_Brick_(placed).png
Plaquage en cuivre > Copper_Plating_(placed).png
Brique d'étain > Tin_Brick_(placed).png
Plaquage d'étain > Tin_Plating_(placed).png
Brique de fer > Iron_Brick_(placed).png
Brique de plomb > Lead_Brick_(placed).png
Brique argentée > Silver_Brick_(placed).png
Brique de tungstène > Tungsten_Brick_(placed).png
Brique dorée > Gold_Brick_(placed).png
Brique de platine > Platinum_Brick_(placed).png
Brique de météorite > Meteorite_Brick_(placed).png
Brique de démonite > Demonite_Brick_(placed).png
Brique de carmitane > Crimtane_Brick_(placed).png
Brique en obsidienne > Obsidian_Brick_(placed).png
Brique de pierre infernale > Hellstone_Brick_(placed).png
Brique de cobalt > Cobalt_Brick_(placed).png
Colonne en palladium > Palladium_Column_(placed).png
Brique de mithril > Mythril_Brick_(placed).png
Bloc de chewing-gum > Bubblegum_Block_(placed).png
Poutre d'adamantite > Adamantite_Beam_(placed).png
Bloc de pierre de titane > Titanstone_Block_(placed).png
Brique de chlorophyte > Chlorophyte_Brick_(placed).png
Plaquage de champignite > Shroomite_Plating_(placed).png
Brique de luminite > Luminite_Brick_(placed).png
Brique de nébuleuse > Nebula_Brick_(placed).png
Brique solaire > Solar_Brick_(placed).png
Brique astrale > Stardust_Brick_(placed).png
Brique du vortex > Vortex_Brick_(placed).png

Bloc de fragment nébuleux > Nebula_Fragment_Block_(placed).png
Bloc de fragment solaire > Solar_Fragment_Block_(placed).png
Bloc de fragment astral > Stardust_Fragment_Block_(placed).png
Bloc de fragment de vortex > Vortex_Fragment_Block_(placed).png

Bloc brillant d'améthyste > Amethyst_Gemspark_Block_(placed).png
Bloc brillant de topaze > Topaz_Gemspark_Block_(placed).png
Bloc brillant de saphir > Sapphire_Gemspark_Block_(placed).png
Bloc brillant d'émeraude > Emerald_Gemspark_Block_(placed).png
Bloc brillant de rubis > Ruby_Gemspark_Block_(placed).png
Bloc brillant de diamant > Diamond_Gemspark_Block_(placed).png
Bloc brillant d'ambre > Amber_Gemspark_Block_(placed).png

Bloc brillant d'améthyste inactif > Offline_Amethyst_Gemspark_Block_(placed).png
Bloc brillant de topaze inactif > Offline_Topaz_Gemspark_Block_(placed).png
Bloc brillant de saphir inactif > Offline_Sapphire_Gemspark_Block_(placed).png
Bloc brillant d'émeraude inactif > Offline_Emerald_Gemspark_Block_(placed).png
Bloc brillant de rubis inactif > Offline_Ruby_Gemspark_Block_(placed).png
Bloc brillant de diamant inactif > Offline_Diamond_Gemspark_Block_(placed).png
Bloc brillant d'ambre inactif > Offline_Amber_Gemspark_Block_(placed).png

Bloc de gelée > Slime_Block_(placed).png
Bloc de gelée rose > Pink_Slime_Block_(placed).png
Bloc de gelée glacée > Frozen_Slime_Block_(placed).png

Bloc de pierre actif > Stone_Block_(placed).png
Bloc de pierre inactif > Inactive_Stone_Block_(placed).png
Tapis roulant (vers la droite) > Conveyor_Belt_(Clockwise)_(placed).gif
Tapis roulant (vers la gauche) > Conveyor_Belt_(Counter_Clockwise)_(placed).gif"""

ref = Reference()

for line in blocklist.split('\n'):
    if line.isnumeric():
        ref.column(int(line))
        continue
    if line.find(' > ') != -1:
        ref.block(*line.split(' > '))
        continue
    ref.block(line)
ref.out('output-fr.svg')
