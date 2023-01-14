from __future__ import annotations

from abc import abstractmethod, ABC
from material import Material
from random_gen import RandomGen

# Generated with https://www.namegenerator.co/real-names/english-name-generator
TRADER_NAMES = [
    "Pierce Hodge",
    "Loren Calhoun",
    "Janie Meyers",
    "Ivey Hudson",
    "Rae Vincent",
    "Bertie Combs",
    "Brooks Mclaughlin",
    "Lea Carpenter",
    "Charlie Kidd",
    "Emil Huffman",
    "Letitia Roach",
    "Roger Mathis",
    "Allie Graham",
    "Stanton Harrell",
    "Bert Shepherd",
    "Orson Hoover",
    "Lyle Randall",
    "Jo Gillespie",
    "Audie Burnett",
    "Curtis Dougherty",
    "Bernard Frost",
    "Jeffie Hensley",
    "Rene Shea",
    "Milo Chaney",
    "Buck Pierce",
    "Drew Flynn",
    "Ruby Cameron",
    "Collie Flowers",
    "Waldo Morgan",
    "Winston York",
    "Dollie Dickson",
    "Etha Morse",
    "Dana Rowland",
    "Eda Ryan",
    "Audrey Cobb",
    "Madison Fitzpatrick",
    "Gardner Pearson",
    "Effie Sheppard",
    "Katherine Mercer",
    "Dorsey Hansen",
    "Taylor Blackburn",
    "Mable Hodge",
    "Winnie French",
    "Troy Bartlett",
    "Maye Cummings",
    "Charley Hayes",
    "Berta White",
    "Ivey Mclean",
    "Joanna Ford",
    "Florence Cooley",
    "Vivian Stephens",
    "Callie Barron",
    "Tina Middleton",
    "Linda Glenn",
    "Loren Mcdaniel",
    "Ruby Goodman",
    "Ray Dodson",
    "Jo Bass",
    "Cora Kramer",
    "Taylor Schultz",
]

class Trader(ABC):
    """
    NOTE: unless specified all methods have a best and worst case complexity of O(1)
    """
    
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.materials: list[Material] = []
        self.buying: Material = None
        self.buying_price: float = None
        
    def __str__(self) -> str:
        return f"<{type(self).__name__}: {self.name} buying [{self.buying}] for {self.buying_price}💰>"
    
    def __repr__(self):
        return self.__str__()

    @classmethod
    def random_trader(cls):
        return RandomTrader(RandomGen.random_choice(TRADER_NAMES))
    
    def get_materials(self):
        return self.materials
    
    def set_all_materials(self, mats: list[Material]) -> None:
        self.materials = mats
        
    def set_materials(self, mats: list[Material]) -> None:
        self.set_all_materials(mats)
    
    def add_material(self, mat: Material) -> None:
        if mat not in self.materials:
            self.materials.append(mat)
            
    # deal handling
    
    def is_currently_selling(self) -> bool:
        return self.buying

    def current_deal(self) -> tuple[Material, float]:
        if self.buying == None: raise ValueError
        return (self.buying, self.buying_price)
    
    def generate_deal(self) -> None:
        self.buying = self.get_market_material()
        self.buying_price = round(2 + 8 * RandomGen.random_float(), 2)

    def stop_deal(self) -> None:
        self.buying = None
    
    @abstractmethod
    def get_market_material(self):
        pass

class RandomTrader(Trader):
    """
    NOTE: unless specified all methods have a best and worst case complexity of O(1)
    """
    
    def get_market_material(self):
        """_summary_

        Returns:
            Material: random material chosen from the avaliable list of materials the trader is buying
        """
        return RandomGen.random_choice(self.get_materials())

class RangeTrader(Trader):
    """
    NOTE: unless specified all methods have a best and worst case complexity of O(1)
    """
    
    def get_market_material(self):
        """_summary_

        Returns:
            Material: random material chosen from the avaliable list of materials the trader is buying within the bounds of lower and upper (see RangeTrader.materials_between)
        """
        lower = RandomGen.randint(0, len(self.get_materials())-1)
        upper = RandomGen.randint(lower, len(self.get_materials())-1)
        return RandomGen.random_choice(self.materials_between(lower, upper))
    
    def materials_between(self, i: int, j: int) -> list[Material]:
        """_summary_

        Args:
            i (int): lower index
            j (int): upper index

        Returns:
            list[Material]: spliced list of materials, bound to the lower and upper indexes (inclusive)
        """
        return self.get_materials()[i:j+1]

class HardTrader(Trader):
    """
    NOTE: unless specified all methods have a best and worst case complexity of O(1)
    """
    
    def get_market_material(self):
        """_summary_

        Returns:
            Material: hardest material to mine in the avaliable list of materials the trader is buying
        """
        hardest_to_mine = None
        hardest_to_mine_value = 0
        for material in self.get_materials():
            if material.mining_rate > hardest_to_mine_value:
                hardest_to_mine = material
        return hardest_to_mine
            

if __name__ == "__main__":
    trader = RangeTrader("Jackson")
    print(trader)
    trader.set_materials([
        Material("Coal", 4.5),
        Material("Diamonds", 3),
        Material("Redstone", 20),
    ])
    trader.generate_deal()
    print(trader)
    trader.stop_deal()
    print(trader)

