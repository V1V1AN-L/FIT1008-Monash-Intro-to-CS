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
        self.balance = self.DEFAULT_EMERALDS if emeralds is None else emeralds
        # extras
        try:
            self.AI = bool(kwargs['AI'])
            self.key_cooldown = int(time.time()*1000)
        except KeyError:
            self.AI = True
        
    def __str__(self) -> str:
        raise NotImplementedError()
    
    def __repr__(self):
        return self.__str__()

    # mutators

    def set_traders(self, traders_list: list[Trader]) -> None:
        self.traders_list = traders_list

    def set_foods(self, foods_list: list[Food]) -> None:
        self.foods_list = foods_list
        
    def set_materials(self, materials_list: list[Material]) -> None:
        self.materials_list = materials_list

    def set_caves(self, caves_list: list[Cave]) -> None:
        self.caves_list = caves_list
        
    def get_traders(self) -> list[Trader]:
        return self.traders_list 

    def get_foods(self) -> list[Food]:
        return self.foods_list 
        
    def get_materials(self) -> list[Material]:
        return self.materials_list 

    def get_caves(self) -> list[Cave]:
        return self.caves_list 

    @classmethod
    def random_player(self) -> Player:
        return Player(RandomGen.random_choice(PLAYER_NAMES), RandomGen.randint(self.MIN_EMERALDS, self.MAX_EMERALDS))

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
    
        return (chosen_food, self.balance, chosen_cave)
    
    def AI_select_food_and_caves(self):
        raise NotImplementedError
    
    
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
