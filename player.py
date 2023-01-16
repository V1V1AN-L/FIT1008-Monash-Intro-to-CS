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

    DEFAULT_EMERALDS = 50

    MIN_EMERALDS = 14
    MAX_EMERALDS = 40

    def __init__(self, name, emeralds=None, **kwargs) -> None:
        self.name = name
        self.set_balance(self.DEFAULT_EMERALDS if emeralds is None else emeralds)
        self.set_hunger() 
        self.set_traders()
        self.set_foods()
        self.set_materials()
        self.set_caves()
        # extras
        try:
            self.AI = bool(kwargs['AI'])
            self.key_cooldown = int(time.time()*1000)
        except KeyError:
            self.AI = True
        
    def __str__(self) -> str:
        return f"{self.name}: {self.get_balance()}💰"
    
    def __repr__(self):
        return self.__str__()
    
    # class methods
    @classmethod
    def random_player(self) -> Player:
        return Player(RandomGen.random_choice(PLAYER_NAMES), RandomGen.randint(self.MIN_EMERALDS, self.MAX_EMERALDS))

    # mutators
    
    # hunger
    def set_hunger(self, hunger: float = None) -> None: 
        if isinstance(hunger, int) or isinstance(hunger, float):
            self.hunger = round(hunger, 2)
        else:
            self.hunger = hunger
        
    def get_hunger(self) -> float:
        self.set_hunger(self.hunger) # makes sure its rounded to two decimal places
        return self.hunger
    
    def clear_hunger(self):
        self.set_hunger(0)
    
    # balance
    def set_balance(self, balance: float = None) -> None:
        if isinstance(balance, int) or isinstance(balance, float):
            self.balance = round(balance, 2)
        else:
            self.balance = balance
        
    def get_balance(self) -> float:
        self.set_balance(self.balance) # makes sure its rounded to two decimal places
        return self.balance

    # traders
    def set_traders(self, traders_list: list[Trader] = None) -> None:
        self.traders_list = traders_list
        
    def get_traders(self) -> list[Trader]:
        return self.traders_list 
    
    # foods
    def set_foods(self, foods_list: list[Food] = None) -> None:
        if foods_list != None:
            self.foods_list: list[Food] = foods_list
        elif self.get_traders() != None:
            self.foods_list: list[Food] = [trader.buying for trader in self.get_traders() if trader.buying != None]
            
    def get_foods(self) -> list[Food]:
        return self.foods_list 
    
    # materials 
    def set_materials(self, materials_list: list[Material] = None) -> None:
        self.materials_list = materials_list
        
    def get_materials(self) -> list[Material]:
        return self.materials_list 
    
    # caves
    def set_caves(self, caves_list: list[Cave] = None) -> None:
        self.caves_list = caves_list

    def get_caves(self) -> list[Cave]:
        return self.caves_list 

    # select_food_and_caves
    def select_food_and_caves(self) -> tuple[Food | None, float, list[tuple[Cave, float]]]: #TODO by Nick
        if self.AI:
            chosen_food, chosen_cave = self.AI_select_food_and_caves()
        else:
            while True:
                chosen_food = self.choose_food_screen()
                try:
                    chosen_cave = self.choose_cave_screen(chosen_food)
                    break
                except:
                    pass
    
        return (chosen_food, self.get_balance(), chosen_cave)
    
    def AI_select_food_and_caves(self):
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
Given that F = #Foods, T = #Traders, C=#Caves, M=#Materials:
Your select_food_and_caves method should have complexity at most O(M + T + F * C * logC)

Documentation Requirement!
For your solution to select_food_and_caves, please leave a lengthy docstring describing the motivation for your approach in full. 
Please use a small example to demonstrate your approach. Additionally, you need to fully justify the complexity of your approach - Give line comments to summarise the complexity of blocks of your code.

        Documentation:
        """
        raise NotImplementedError
        chosen_food, chosen_cave = None, None
        return chosen_food, chosen_cave
        
    
    
    # MANUAL CONTROL OF PLAYERS
        
    def refresh_key_cooldown(self):
        while True:
            try:
                if self.key_cooldown <= int(time.time()*1000):
                    self.key_cooldown = int(time.time()*1000) + 100
                    return True
                return False
            except AttributeError:
                self.key_cooldown = int(time.time()*1000) 
    
    def choose_food_screen(self):
        clearConsole()
        self.title = 'Food'
        foods = FOOD_NAMES  
        dark = '\033[90m'
        clear = '\033[0m'
        choice = 0
        while True:
            if choice < 3:
                chosen_range = range(0, 8)
            elif choice > len(foods[i])-8:
                chosen_range = range(len(foods[i])-8, len(foods[i]))
            else:
                chosen_range = range(choice-3, choice + 5)
            for i in chosen_range:
                food = f"{foods[i]}"
                if i == choice:
                    food += ' <<'
                    print(
f"""{clear}{medium_text_print(food, 1)}{dark}
{clear}{medium_text_print(food, 2)}{dark}  
{' '*get_screensize()}""")
                else:
                    print(
f"""{dark}{medium_text_print(food, 1)}
{medium_text_print(food, 2)}{dark}   
{' '*get_screensize()}""")
            # get input or not
            pressed_key = keyboard_wait()
            if self.refresh_key_cooldown() and pressed_key == 'up' and choice > 0:
                choice -= 1
            elif self.refresh_key_cooldown() and pressed_key == 'down' and choice < len(foods):
                choice += 1
            elif self.refresh_key_cooldown() and pressed_key == 'enter':
                return foods[choice]
            go_back()
        
    def choose_cave_screen(self):
        clearConsole()
        self.title = 'Caves'
        caves = CAVE_NAMES  
        dark = '\033[90m'
        clear = '\033[0m'
        choice = 0
        while True:
            if choice < 3:
                chosen_range = range(0, 8)
            elif choice > len(caves[i])-8:
                chosen_range = range(len(caves[i])-8, len(caves[i]))
            else:
                chosen_range = range(choice-3, choice + 5)
            for i in chosen_range:
                cave = f"{caves[i]}"
                if i == choice:
                    cave += ' <<'
                    print(
f"""{clear}{medium_text_print(cave, 1)}{dark}
{clear}{medium_text_print(cave, 2)}{dark}  
{' '*get_screensize()}""")
                else:
                    print(
f"""{dark}{medium_text_print(cave, 1)}
{medium_text_print(cave, 2)}{dark}   
{' '*get_screensize()}""")
            # get input or not
            pressed_key = keyboard_wait()
            if self.refresh_key_cooldown() and pressed_key == 'up' and choice > 0:
                choice -= 1
            elif self.refresh_key_cooldown() and pressed_key == 'down' and choice < len(caves):
                choice += 1
            elif self.refresh_key_cooldown() and pressed_key == 'enter':
                return caves[choice]
            go_back()
    
    def display_title(self):
        title = self.title
        #
        screensize = get_screensize()
        big_text_len = len(big_text_print(title, 1))
        title_white_space = ' '*(screensize//2-(big_text_len//2)-1)
        #
        print(
f"""{title_white_space}{big_text_print(title, 1)}{title_white_space}
{title_white_space}{big_text_print(title, 2)}{title_white_space}
{title_white_space}{big_text_print(title, 3)}{title_white_space} 
{title_white_space}{big_text_print(title, 4)}{title_white_space} 
{title_white_space}{big_text_print(title, 5)}{title_white_space}    
{'-'*screensize}
""")
        




if __name__ == "__main__":
    player = Player("Alex", emeralds=1000)
    print(player.choose_food_screen())
