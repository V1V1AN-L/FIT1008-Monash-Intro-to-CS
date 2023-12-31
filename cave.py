from __future__ import annotations
from random_gen import *

from material import Material

# List of cave names from https://en.uesp.net/wiki/Skyrim:Caves. Thanks Skyrim.
CAVE_NAMES = [
    "Ashfall's Tear", # A hidden Tribunal Temple shrine to the Goddess Almalexia in a cave north of Raven Rock.
    "Benkongerike", # A medium-sized cave southeast of Saering's Watch and northwest of Headwaters of Harstrad containing bristlebacks and rieklings.
    "Blackbone Isle Grotto", # A small cave connected to the sea, situated on Blackbone Isle.
    "Bleakcoast Cave", # A small cave southeast of Winterhold and directly east of the Shrine of Azura occupied by frost trolls.
    "Blind Cliff Cave", # A medium-sized cave southwest of Karthwasten along the banks of the Karth River occupied by Forsworn.
    "Bloated Man's Grotto", # A small cave inhabited by spriggans and cave bears.
    "Bloodchill Cavern", # A vampiric player home in Winterhold, southeast of Snowpoint Beacon.
    "Bonechill Passage", # A small cave containing monsters, located east of Falkreath and to the southwest of Helgen.
    "Boulderfall Cave", # A small cave inhabited by leveled necromancers.
    "Brinewater Grotto", # A small cave on the coast between Solitude Lighthouse and Broken Oar Grotto.
    "Bristleback Cave", # A medium-sized cave due northwest of Broken Tusk Mine containing bristlebacks and rieklings.
    "Brittleshin Pass", # A small passage through the mountains between Whiterun Hold and Falkreath Hold.
    "Broken Fang Cave", # A small cave situated south of Swindler's Den (west of Whiterun).
    "Broken Helm Hollow", # A small cave in the southeast corner of The Rift occupied by bandits.
    "Broken Oar Grotto", # A large cave connected to the sea, located north of Solitude and northwest of Brinewater Grotto.
    "Bronze Water Cave", # A one-chamber cave west of Windhelm on the northern shore of Lake Yorgrim.
    "Brood Cavern", # A small cave high in the mountains southwest of Morthal.
    "Bruca's Leap Redoubt", # A small cave inhabited by Forsworn.
    "Castle Karstaag Caverns", # A medium-sized cave on the north coast of Solstheim containing bristlebacks and rieklings.
    "Castle Karstaag Ruins", # An icy clearing outside Castle Karstaag Caverns.
    "Chillwind Depths", # A medium-sized cave south of Dragon Bridge, on the border of Hjaalmarch and The Reach.
    "Clearspring Cave", # A small cave overlooking Eastmarch occupied by a troll.
    "Cold Rock Pass", # A small passage through a mountain northwest of Whiterun.
    "Coldcinder Cave", # A small cave with two entrances: one via a grate in the Bulwark Jail, and the other through a trap door atop the cliff just southeast of Raven Rock, near the top of the Bulwark.
    "Cragslane Cavern", # A small cave being used by bandits for skooma operations and animal blood sports.
    "Cragwallow Slope", # A medium-sized cave southeast of Windhelm home to conjurers and atronachs.
    "Cronvangr Cave", # A medium-sized cave southwest of Kynesgrove, inhabited by frostbite spiders and vampires.
    "Crystaldrift Cave", # A small cave that serves as the resting place for an insane Bosmer, with a shrine Kynareth built to watch over him and to bring peace to weary travelers.
    "Darkfall Cave", # A small cave just south-southwest of the Orc stronghold Mor Khazgur.
    "Darkfall Passage", # A small cave which is only accessible through Darkfall Cave, and is the only access to the Forgotten Vale.
    "Darkshade", # A small cave located just off of the base of the White River waterfall east of Valtheim Towers.
    "Darkwater Pass", # A medium-sized cave near Darkwater Crossing home to Falmer and chaurus.
    "Dimhollow Crypt", # A large cave southwest of Dawnstar where Serana is trapped.
    "Duskglow Crevice", # A small cave east of Fort Dunstad, occupied mainly by Falmer and chaurus.
    "Eldergleam Sanctuary", # An underground grove and worship site of the followers of Kynareth.
    "Fallowstone Cave", # A small cave with an exit to Giant's Grove, located in the Velothi Mountains northeast of Riften and a short distance north of Lost Prospect Mine.
    "Forebears' Holdout", # A small cave southeast of Dragon Bridge.
    "Forsaken Cave", # A medium-sized cave located west of Windhelm.
    "Frossel", # A small cave on a peninsula east of Haknir's Shoal and north of Skaal Village containing bristlebacks and rieklings.
    "Frostmoon Crag", # A small camp under a rock overhang south of Mount Moesring and northeast of the Abandoned Lodge inhabited by werewolves.
    "Frostroot Cave", # A cave in Eastmarch, north of Kagrenzel.
    "Glacial Cave", # A small cave north of Benkongerike, carved into the glacial cliff face along the northeastern coast, containing rieklings and horkers.
    "Glenmoril Coven", # A small cave far to the northwest of Falkreath inhabited by a group of unique hagravens, the Glenmoril Witches.
    "Gloomreach", # A medium-sized cave in the Reach containing chaurus and Falmer.
    "Graywinter Watch", # A one-chamber cave underneath the Ritual Stone (east of Whiterun) occupied by trolls.
    "Greywater Grotto", # A small cave far east of Falkreath, located south-southwest of Helgen, containing leveled predatory animals.
    "Gromm's Pass", # A small cave located in the Rift, south of Forelhost.
    "Haemar's Shame", # A medium-sized cave that is home to vampiric worshippers of Clavicus Vile.
    "Halldir's Cairn", # A small cave and tomb in the southernmost part of Skyrim that was built to house the remains of the fierce Halldir.
    "Hob's Fall Cave", # A small cave on the coast between Winterhold and Dawnstar inhabited by leveled warlocks and skeletons.
    "Honeystrand Cave", # A small cave occupied by bears.
    "Hrothmund's Barrow", # A small cave southwest of Benkongerike.
    "Iron Tusk Cave", # A small cave on the island of Giant's Tooth.
    "Liar's Retreat", # A small cave and connected underground cellar northwest of Broken Tower Redoubt and northeast of Karthwasten.
    "Lost Echo Cave", # A small cave near the northwestern coast of Haafingar occupied by Falmer.
    "Lost Knife Hideout", # A large cave that serves as the hideout for the Lost Knife bandits.
    "Mara's Eye Den", # A small cave found on the middle island of Mara's Eye Pond.
    "Moss Mother Cavern", # A small, open-roofed cavernous grove lush with many kinds of flora and fungi, located due north of Hunter's Rest and northwest of Half-Moon Mill.
    "Movarth's Lair", # A small cave north of Morthal inhabited by vampires.
    "Nightingale Hall", # The home of the Nightingales between Riften and the Shadow Stone.
    "Orotheim", # A small cave that is home to bandits intent on poaching mammoths.
    "Pinemoon Cave", # A small cave located to the northwest of Dragon Bridge and east of Volskygge.
    "Pinepeak Cavern", # A small cave along the Treva River occupied by bears.
    "Purewater Run", # A small cave south-southeast of Markarth containing slaughterfish.
    "Ravenscar Hollow", # A small cave inhabited by hagravens west of the Thalmor Embassy and due east of the Steed Stone.
    "Reachcliff Cave", # A small cave filled with draugr located northeast of Dushnikh Yal and southeast of Markarth.
    "Reachwater Rock", # A small cave east-southeast of Markarth and south of Sky Haven Temple, containing draugr.
    "Rebel's Cairn", # A small cave located in The Reach between the Sundered Towers and Bleakwind Bluff.
    "Red Eagle Redoubt", # A small cave and two exterior camps, one small and one sprawling, all occupied by Forsworn located east of Markarth.
    "Redoran's Retreat", # A small cave northwest of Whiterun occupied by bandits.
    "Rimerock Burrow", # A small cave located at the northwestern edge of Skyrim.
    "Runoff Caverns", # A large cave in the Reach, west of Lost Valley Redoubt.
    "Ruunvald Excavation", # A medium-sized cave east-southeast of Shor's Watchtower and north-northeast of Riften.
    "Septimus Signus's Outpost", # A small cave on a small remote icy island off the north coast of Skyrim, where Septimus Signus has made his home.
    "Shadowgreen Cavern", # A small cave northwest of Solitude, which is home to leveled spriggans and animals.
    "Shimmermist Cave", # A medium-sized cave northeast of Whiterun occupied by Falmer.
    "Sightless Pit", # A medium-sized cave in Winterhold occupied by Falmer.
    "Snapleg Cave", # A medium-sized cave carved into the side of a mountain.
    "Soljund's Sinkhole", # A medium-sized moonstone mine east of Sky Haven Temple with a smelter near the entrance.
    "Southfringe Sanctum", # A small cave occupied by the conjurer Bashnag and his coven.
    "Steepfall Burrow", # A small cave containing animals on the north coast of Haafingar.
    "Stillborn Cave", # A small cave north-northwest of Windhelm, on the other side of the mountains from the city.
    "Stony Creek Cave", # A small cave located in the southeastern corner of Eastmarch that is occupied by bandits.
    "Sunderstone Gorge", # A medium-sized cave west of Bloated Man's Grotto occupied by warlocks.
    "Swindler's Den", # A small cave between Whiterun and Rorikstead occupied by bandits.
    "Tolvald's Cave", # A large cave in the Velothi Mountains, northeast of Shor's Stone and south-southeast of Ansilvund.
    "Uttering Hills Cave", # A small cave in the mountains southwest of Windhelm occupied by bandits.
    "White River Watch", # A small cave east-northeast of Honningbrew Meadery and southwest of the Ritual Stone occupied by the White River bandits.
    "Wolfskull Cave", # A medium-sized cave west of Solitude filled with necromancers or bandits.
    "Yngvild", # A medium-sized cave on an island east-northeast of Dawnstar in the far northern reaches of Skyrim.
]

class Cave:
    """
    NOTE: unless specified all methods have a best and worst case complexity of O(1)

    Class Attribute:
        MIN_MATERIALS: minimum amount of material in the cave
        MAX_MATERIALS: maximum amount of material in the cave

    attribute:
        name: name of the cave
        material: material stored inside the cave (one only @cave)
        quantity: amount of the material that can be mined in the cave
    """
    
    MIN_MATERIALS = 1
    MAX_MATERIALS = 10
    
    def __init__(self, name: str, material: Material, quantity: float = 0.0) -> None:
        """ Initialization """
        self.name = name
        self.material = material
        self.quantity = quantity
        
    def __str__(self) -> str:
        """ Formatted string representation """
        return f"{self.name}: {int(self.quantity)} {self.material.get_material_plural(int(self.quantity))}"
        
    def __repr__(self):
        """ Formatted string representation """
        return self.__str__()
    
    def __eq__(self, other):
        """ Checking whether two caves has the same name and material or not """
        return self.name == other.name and self.material == other.material
    
    # material
    
    def get_material(self):
        """ Get the material inside the cave """
        return self.material
    
    # quantity
    
    def round_quantity(self):
        """ Rounding the quantity of the material """
        self.quantity = round(self.quantity, 4)
    
    def add_quantity(self, amount: float) -> None:
        """ Add more quantity of materials inside the cave """
        self.quantity += amount
        self.round_quantity()
    
    def remove_quantity(self, amount: float) -> None:
        """ Decrease the quantity of material  inside the caves """
        if amount > self.quantity:
            self.clear_quantity()
        else:
            self.quantity -= amount
            self.round_quantity()
        
    def clear_quantity(self):
        """ Reset quantity of material to zero """
        self.quantity = 0

    def get_quantity(self) -> float:
        """ Get the quantity of materials inside the caves """
        self.round_quantity()
        return self.quantity
    
    def get_quantity_given_energy_spent(self, energy) -> float:
        """ Calculate the quantity of materials depends on how many energy spent by the player """
        if energy <= 0:
            return 0
        quantity = round(energy/self.material.mining_rate, 4)
        if quantity > self.get_quantity():
            quantity = self.get_quantity()
        return quantity
    
    def calculate_total_hunger_spent(self, quantity: float = None):
        """ Calculate the total hunger that player spent when mining in this cave """
        if quantity != None:
            return int(quantity * self.material.mining_rate)
        return int(self.get_quantity() * self.material.mining_rate)
        

    @classmethod
    def random_cave(cls, material_list: list[Material]) -> Cave:
        """
        Create an object of this class with two option
        first: if the material_list consists one Material only
        second: if the material_list contains more than one Material, we will choose random from that.

        """
        if isinstance(material_list, Material):
            return Cave(RandomGen.random_choice(CAVE_NAMES), material_list, RandomGen.randint(cls.MIN_MATERIALS, cls.MAX_MATERIALS))
        elif isinstance(material_list, list):
            chosen_material = RandomGen.random_choice(material_list)
            return Cave(RandomGen.random_choice(CAVE_NAMES), chosen_material, RandomGen.randint(cls.MIN_MATERIALS, cls.MAX_MATERIALS))
        

if __name__ == "__main__":
    print(Cave.random_cave([Material.random_material() for _ in range(5)]))
    print(Cave("Mt Coronet", Material("Coal", 4.5), 3))
