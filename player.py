from __future__ import annotations
from random_gen import *
from graphics_module import *
from cave import *
from material import *  
from food import *
from trader import Trader


# List taken from https://minecraft.fandom.com/wiki/Mob
PLAYER_NAMES = [
    "Steve",
    "Alex",
    "ɘᴎiɿdoɿɘH",
    "Allay",
    "Axolotl",
    "Bat",
    "Cat",
    "Chicken",
    "Cod",
    "Cow",
    "Donkey",
    "Fox",
    "Frog",
    "Glow Squid",
    "Horse",
    "Mooshroom",
    "Mule",
    "Ocelot",
    "Parrot",
    "Pig",
    "Pufferfish",
    "Rabbit",
    "Salmon",
    "Sheep",
    "Skeleton Horse",
    "Snow Golem",
    "Squid",
    "Strider",
    "Tadpole",
    "Tropical Fish",
    "Turtle",
    "Villager",
    "Wandering Trader",
    "Bee",
    "Cave Spider",
    "Dolphin",
    "Enderman",
    "Goat",
    "Iron Golem",
    "Llama",
    "Panda",
    "Piglin",
    "Polar Bear",
    "Spider",
    "Trader Llama",
    "Wolf",
    "Zombified Piglin",
    "Blaze",
    "Chicken Jockey",
    "Creeper",
    "Drowned",
    "Elder Guardian",
    "Endermite",
    "Evoker",
    "Ghast",
    "Guardian",
    "Hoglin",
    "Husk",
    "Magma Cube",
    "Phantom",
    "Piglin Brute",
    "Pillager",
    "Ravager",
    "Shulker",
    "Silverfish",
    "Skeleton",
    "Skeleton Horseman",
    "Slime",
    "Spider Jockey",
    "Stray",
    "Vex",
    "Vindicator",
    "Warden",
    "Witch",
    "Wither Skeleton",
    "Zoglin",
    "Zombie",
    "Zombie Villager",
    "H̴͉͙̠̥̹͕͌̋͐e̸̢̧̟͈͍̝̮̹̰͒̀͌̈̆r̶̪̜͙̗̠̱̲̔̊̎͊̑̑̚o̷̧̮̙̗̖̦̠̺̞̾̓͆͛̅̉̽͘͜͝b̸̨̛̟̪̮̹̿́̒́̀͋̂̎̕͜r̸͖͈͚̞͙̯̲̬̗̅̇̑͒͑ͅi̶̜̓̍̀̑n̴͍̻̘͖̥̩͊̅͒̏̾̄͘͝͝ę̶̥̺̙̰̻̹̓̊̂̈́̆́̕͘͝͝"
]

class Player():
    
    """
    NOTE: unless specified all methods have a best and worst case complexity of O(1)
    """

    DEFAULT_EMERALDS = 50

    MIN_EMERALDS = 20
    MAX_EMERALDS = 100

    def __init__(self, name, emeralds: float = None) -> None:
        self.name = name
        self.set_balance(self.DEFAULT_EMERALDS if emeralds is None else emeralds)
        self.set_hunger() 
        self.set_traders()
        self.set_foods()
        self.set_caves()
        
    def __str__(self) -> str:
        return f"{self.name}: {self.get_balance()}💰"
    
    def __repr__(self):
        return self.__str__()
    
    # class methods
    @classmethod
    def random_player(self) -> Player:
        return Player(RandomGen.random_choice(PLAYER_NAMES), RandomGen.randint(self.MIN_EMERALDS, self.MAX_EMERALDS))

    # mutators
    
    def set_materials(self, materials):
        pass
    
    # hunger
    def set_hunger(self, hunger: float = 0) -> None: 
        if isinstance(hunger, int) or isinstance(hunger, float):
            self.hunger = round(hunger, 2)
        else:
            self.hunger = hunger
        
    def get_hunger(self) -> float:
        self.set_hunger(self.hunger) # makes sure its rounded to two decimal places
        return self.hunger
    
    def decrease_hunger(self, hunger: float = 0) -> None: 
        if isinstance(hunger, int) or isinstance(hunger, float):
            self.hunger -= round(hunger, 2)
        else:
            self.hunger -= hunger
    
    def clear_hunger(self):
        self.set_hunger(0)
        
    def check_hunger(self):
        if self.hunger <= 0:
            self.clear_hunger()
            return True
        return False
        
    
    # balance
    def set_balance(self, balance: float = 0) -> None:
        if isinstance(balance, int) or isinstance(balance, float):
            self.balance = round(balance, 2)
        else:
            self.balance = balance
        
    def get_balance(self) -> float:
        self.set_balance(self.balance) # makes sure its rounded to two decimal places
        return self.balance
    
    def increase_balance(self, balance: float = 0):
        if isinstance(balance, int) or isinstance(balance, float):
            self.balance += round(balance, 2)
        else:
            self.balance += balance
            
    def decrease_balance(self, balance: float = 0):
        if isinstance(balance, int) or isinstance(balance, float):
            self.balance -= round(balance, 2)
        else:
            self.balance -= balance
    

    # traders
    def set_traders(self, traders_list: list[Trader] = None) -> None:
        self.traders_list = traders_list
        
    def get_traders(self) -> list[Trader]:
        return self.traders_list 
    
    
    # foods
    def set_foods(self, foods_list: list[Food] = None) -> None:
        if foods_list != None:
            self.foods_list: list[Food] = [food for food in foods_list if isinstance(food, Food)]
        elif self.get_traders() != None:
            self.foods_list: list[Food] = []
        else:
            self.foods_list = foods_list
            
    def get_foods(self) -> list[Food]:
        return self.foods_list     
    
    # caves
    def set_caves(self, caves_list: list[Cave] = None) -> None:
        self.caves_list = caves_list

    def get_caves(self) -> list[Cave]:
        return self.caves_list 

    # (SOLO) select_food_and_caves
    def select_food_and_caves(self, offered_food: Food = None) -> tuple[Food | None, float, list[tuple[Cave, float]]]: 
        """_summary_
        
        Returns :
            tuple: _description_
        
        brief on function:
Given that the player has access to the materials, caves, and traders given through the relevant methods in the player class (which you need to implement), 
we want to implement the method select_food_and_caves, which generates a tuple containing 3 objects:
- The food which this player will buy
- The emerald balance after this player has made their move
- A list of all caves plundered on their journey, paired with the quantity of each material mined.

The choice the player makes should be optimal (Achieving the highest balance of emeralds possible in a single day) The method should not change the existing quantities of any caves, or any statistics of any material/cave/trader object.

Complexity Requirement!
Given that F = #Foods, T = #Traders, C = #Caves, M = #Materials:
Your select_food_and_caves method should have complexity at most O(M + T + F * C * logC)

Documentation Requirement!
For your solution to select_food_and_caves, please leave a lengthy docstring describing the motivation for your approach in full. 
Please use a small example to demonstrate your approach. Additionally, you need to fully justify the complexity of your approach - Give line comments to summarise the complexity of blocks of your code.

Approaches:
SOLO food:
    Returns the food that has the most hunger filling while the balance is above 0

SOLO caves:
    Returns caves in order of mining based on how much profit you can make from them
    
SOLO Complexity: (best & worst) = O(T + F + C)


MULTIPLAYER food:
    If the player can afford the food, they buy it

MULTIPLAYER caves:
    As you can only choose one cave, you want the most amount of profit possible from a single cave

MULTIPLAYER Complexity: (best & worst) = O(C + T)
        """
        self.generate_material_price_map() # O(T)
        
        if isinstance(offered_food, Food):
            chosen_food, chosen_caves = self.multiplayer_select_food_and_caves(offered_food)
        else:
            chosen_food, chosen_caves = self.solo_select_food_and_caves()
    
        return (chosen_food, self.get_balance(), chosen_caves)
    
    
    def solo_select_food_and_caves(self) -> tuple[Food, list[Cave]]:
        chosen_food = self.choose_food()
        chosen_caves = self.choose_caves()
        return chosen_food, chosen_caves
    
    def multiplayer_select_food_and_caves(self, offered_food) -> tuple[Food|None, Cave]:
        chosen_food = self.multiplayer_choose_food(offered_food)
        chosen_cave = self.multiplayer_choose_caves()
        return chosen_food, chosen_cave
    
    # SOLO
    
    def choose_food(self) -> Food:
        """_summary_

        Returns:
            Food: chosen food
            
        COMPLEXITY (best & worst) = O(F)
        """
        hunger = 0
        chosen_food: Food = None
        for food in self.get_foods():
            if food.hunger_bars > hunger and food.price <= self.get_balance():
                hunger = food.hunger_bars
                chosen_food: Food = food
        return chosen_food
    
    def choose_caves(self) -> list[Cave]:
        """_summary_

        Returns:
            list[Cave]: list of caves in order of mining to 
            
        Returns caves in order of mining based on how much profit you can make from them
            
        COMPLEXITY COMPLEXITY (best & worst) = O(C)
        """
        player_hunger_spent = 0
        caves_and_profit = {}
        for cave in self.get_caves():
            profit_made = round(float(self.get_material_price(cave.get_material())*cave.get_quantity()), 2)
            caves_and_profit[profit_made] = cave
            
        chosen_caves = []
        while player_hunger_spent <= self.get_hunger():
            max_value = max(list(caves_and_profit.keys()))
            chosen_cave = caves_and_profit[max_value]
            del caves_and_profit[max_value]
            chosen_caves.append(chosen_cave)
            player_hunger_spent += cave.get_material().mining_rate*cave.get_quantity()
        
        return chosen_caves
    
    
    # MULTI
    
    def multiplayer_choose_food(self, offered_food: Food) -> Food | None:
        """_summary_

        Args:
            offered_food (Food): food offered to players during a multiplayer game

        Returns:
            Food|None: food chosen for a multiplayer game
            
        COMPLEXITY (best & worst) = O(1)
        """
        if offered_food.price <= self.get_balance():
            return offered_food
        return None
        
    def multiplayer_choose_caves(self) -> Cave:
        """_summary_

        Returns:
            _type_: _description_
            
        COMPLEXITY (best & worst) = O(C)
        """
        chosen_cave = None
        max_profit = 0
        chosen_quantity = 0
        for cave in self.get_caves():
            try:
                quantity = cave.get_quantity_given_energy_spent(self.get_hunger())
                profit = self.get_material_price(cave.get_material())*quantity
            except KeyError:
                profit = 0
            if profit > max_profit:
                chosen_quantity = quantity
                chosen_cave = cave
        return [chosen_cave, chosen_quantity]
    
    # helper methods
    
    def get_material_price(self, material: Material) -> float:
        try:
            return self.material_price_map[f"{material}"]
        except KeyError:
            return 0.00
    
    def generate_material_price_map(self):
        """_summary_

        Returns:
            _type_: _description_
            
        COMPLEXITY (best & worst) = O(T), T = amount of traders avaliable to trade
        """
        material_map = {}
        for trader in self.get_traders():
            try:
                material, selling_price = trader.current_deal()
                material_map[f"{material}"] = selling_price
            except ValueError:
                pass
            
        
        self.material_price_map = material_map
        return self.material_price_map
    