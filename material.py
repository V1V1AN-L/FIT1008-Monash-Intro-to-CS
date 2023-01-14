from random_gen import RandomGen
from graphics_module import *

# Material names taken from https://minecraft-archive.fandom.com/wiki/Items
RANDOM_MATERIAL_NAMES = [
    "Arrow",
    "Axe",
    "Bow",
    "Bucket",
    "Carrot on a Stick",
    "Clock",
    "Compass",
    "Crossbow",
    "Exploration Map",
    "Fire Charge",
    "Fishing Rod",
    "Flint and Steel",
    "Glass Bottle",
    "Dragon's Breath",
    "Hoe",
    "Lead",
    "Map",
    "Pickaxe",
    "Shears",
    "Shield",
    "Shovel",
    "Sword",
    "Saddle",
    "Spyglass",
    "Totem of Undying",
    "Blaze Powder",
    "Blaze Rod",
    "Bone",
    "Bone meal",
    "Book",
    "Book and Quill",
    "Enchanted Book",
    "Bowl",
    "Brick",
    "Clay",
    "Coal",
    "Charcoal",
    "Cocoa Beans",
    "Copper Ingot",
    "Diamond",
    "Dyes",
    "Ender Pearl",
    "Eye of Ender",
    "Feather",
    "Spider Eye",
    "Fermented Spider Eye",
    "Flint",
    "Ghast Tear",
    "Glistering Melon",
    "Glowstone Dust",
    "Gold Ingot",
    "Gold Nugget",
    "Gunpowder",
    "Ink Sac",
    "Iron Ingot",
    "Iron Nugget",
    "Lapis Lazuli",
    "Leather",
    "Magma Cream",
    "Music Disc",
    "Name Tag",
    "Nether Bricks",
    "Paper",
    "Popped Chorus Fruit",
    "Prismarine Crystal",
    "Prismarine Shard",
    "Rabbit's Foot",
    "Rabbit Hide",
    "Redstone",
    "Seeds",
    "Beetroot Seeds",
    "Nether Wart Seeds",
    "Pumpkin Seeds",
    "Wheat Seeds",
    "Slimeball",
    "Snowball",
    "Spawn Egg",
    "Stick",
    "String",
    "Wheat",
    "Netherite Ingot",
]

class Material:
    """
    NOTE: unless specified all methods have a best and worst case complexity of O(1)
    """
    
    def __init__(self, name: str, mining_rate: float) -> None:
        assert name in RANDOM_MATERIAL_NAMES, "invalid name"
        self.name = name
        self.mining_rate = mining_rate
    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: string representation
        """
        return f"{self.name}: {int(self.mining_rate)}🍗/💎"
    
    def get_material_plural(self, amount: int = 2):
        mapping = {
        "Arrow":"Arrows",
        "Axe":"Axes",
        "Bow":"Bows",
        "Bucket":"Buckets",
        "Carrot on a Stick":"Carrots on a Stick",
        "Clock":"Clocks",
        "Compass":"Compass'",
        "Crossbow":"Crossbows",
        "Exploration Map":"Exploration Maps",
        "Fire Charge":"Fire Charges",
        "Fishing Rod":"Fishing Rods",
        "Flint and Steel":"Flints and Steels",
        "Glass Bottle":"Glass Bottles",
        "Dragon's Breath":"Dragon's Breath",
        "Hoe":"Hoes",
        "Lead":"Leads",
        "Map":"Maps",
        "Pickaxe":"Pickaxe",
        "Shears":"Pair of Shears",
        "Shield":"Shields",
        "Shovel":"Shovels",
        "Sword":"Swords",
        "Saddle":"Saddles",
        "Spyglass":"Spyglasses",
        "Totem of Undying":"Totems of Undying",
        "Blaze Powder":"Blaze Powder",
        "Blaze Rod":"Blaze Rods",
        "Bone":"Bones",
        "Bone meal":"Bone meal",
        "Book":"Books",
        "Book and Quill":"Book and Quills",
        "Enchanted Book":"Enchanted Books",
        "Bowl":"Bowls",
        "Brick":"Bricks",
        "Clay":"Clay",
        "Coal":"Coal",
        "Charcoal":"Charcoal",
        "Copper Ingot":"Copper Ingot",
        "Diamond":"Diamonds",
        "Ender Pearl":"Ender Pearls",
        "Eye of Ender":"Eyes of Ender",
        "Feather":"Feather",
        "Spider Eye":"Spider Eyes",
        "Fermented Spider Eye":"Fermented Spider Eyes",
        "Flint":"Flint",
        "Ghast Tear":"Ghast Tears",
        "Glistering Melon":"Glistering Melons",
        "Glowstone Dust":"Glowstone Dust",
        "Gold Ingot":"Gold Ingots",
        "Gold Nugget":"Gold Nuggets",
        "Gunpowder":"Gunpowder",
        "Ink Sac":"Ink Sacs",
        "Iron Ingot":"Iron Ingots",
        "Iron Nugget":"Iron Nuggets",
        "Lapis Lazuli":"Lapis Lazuli",
        "Leather":"Leather",
        "Magma Cream":"Magma Cream",
        "Music Disc":"Music Discs",
        "Name Tag":"Name Tags",
        "Paper":"Paper",
        "Popped Chorus Fruit":"Popped Chorus Fruits",
        "Prismarine Crystal":"Prismarine Crystals",
        "Prismarine Shard":"Prismarine Shards",
        "Rabbit's Foot":"Rabbit's Feet",
        "Rabbit Hide":"Rabbit Hide",
        "Redstone":"Redstone",
        "Slimeball":"Slimeballs",
        "Snowball":"Snowballs",
        "Spawn Egg":"Spawn Eggs",
        "Stick":"Sticks",
        "String":"String",
        "Wheat":"Wheat",
        "Netherite Ingot":"Netherite Ingots",
        }
        exceptions = ['Shears']
        try:
            plural = mapping[self.name]
            if amount == 1 or self.name in exceptions:   
                return plural
            return self.name
        except KeyError:
            return self.name[:-1] # gets rid of the 's' at the end of the name

    @classmethod
    def random_material(cls):
        raise NotImplementedError()


        
