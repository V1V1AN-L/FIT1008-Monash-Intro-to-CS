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

    Class Attributes:
        DEFAULT_EMERALDS: Default amount of emeralds that player hold in the first round
        MIN_EMERALDS: Lower bound of amount of emeralds when initialize the player
        MAX_EMERALDS: upper bound of amount of emeralds when initialize the player

    Attribute:
        name: name of the player
        balance: emerald balance that the player have
        hunger: Hunger indicator for the player
        trader: Trader that player wants to trade with
        food_list: List of foods that player can choose from
        caves_list: List of caves that player can choose from

        AI: mode of the player (True/False)
        key_cooldown: cooldown time
    """

    DEFAULT_EMERALDS = 50

    MIN_EMERALDS = 14
    MAX_EMERALDS = 40

    def __init__(self, name, emeralds=None, **kwargs) -> None:
        """ Initialization """
        self.name = name
        self.set_balance(self.DEFAULT_EMERALDS if emeralds is None else emeralds)
        self.set_hunger() 
        self.set_traders()
        self.set_foods()
        self.set_caves()
        # extras
        try:
            self.AI = bool(kwargs['AI'])
            self.key_cooldown = int(time.time()*1000)
        except KeyError:
            self.AI = True
        
    def __str__(self) -> str:
        """ Formatted string representation """
        return f"{self.name}: {self.get_balance()}💰"
    
    def __repr__(self):
        """ Formatted string represntation """
        return self.__str__()
    
    # class methods
    @classmethod
    def random_player(self) -> Player:
        """ Create the Player object """
        return Player(RandomGen.random_choice(PLAYER_NAMES), RandomGen.randint(self.MIN_EMERALDS, self.MAX_EMERALDS))

    # mutators
    
    def set_materials(self, materials):
        pass
    
    # hunger
    def set_hunger(self, hunger: float = 0) -> None:
        """ Set the hunger value for player """
        if isinstance(hunger, int) or isinstance(hunger, float):
            self.hunger = round(hunger, 2)
        else:
            self.hunger = hunger
        
    def get_hunger(self) -> float:
        """ Get the hunger value of the player """
        self.set_hunger(self.hunger) # makes sure its rounded to two decimal places
        return self.hunger
    
    def decrease_hunger(self, hunger: float = 0) -> None:
        """ Decrease the hunger once player consume food """
        if isinstance(hunger, int) or isinstance(hunger, float):
            self.hunger -= round(hunger, 2)
        else:
            self.hunger -= hunger
    
    def clear_hunger(self):
        """ Reset hunger value into zero """
        self.set_hunger(0)
        
    def check_hunger(self):
        """ Check whether """
        if self.hunger <= 0:
            self.clear_hunger()
            return True
        return False
        
    
    # balance
    def set_balance(self, balance: float = 0) -> None:
        """ Rounding the emerald balance of the player by 2 number behind the decimal """
        if isinstance(balance, int) or isinstance(balance, float):
            self.balance = round(balance, 2)
        else:
            self.balance = balance
        
    def get_balance(self) -> float:
        """ Get the emerald balance of the player"""
        self.set_balance(self.balance) # makes sure its rounded to two decimal places
        return self.balance
    
    def increase_balance(self, balance: float = 0):
        """ Increase emerald balance of the player"""
        self.set_balance(self.balance + balance)

    def decrease_balance(self, balance: float = 0):
        """ Decrease emerald balance of the player """
        self.set_balance(self.balance - balance)
    

    # traders
    def set_traders(self, traders_list: list[Trader] = None) -> None:
        """ Set the trader for each turn """
        self.traders_list = traders_list
        
    def get_traders(self) -> list[Trader]:
        """ Get the list of traders """
        return self.traders_list 
    
    
    # foods
    def set_foods(self, foods_list: list[Food] = None) -> None:
        """ Set the list of foods that is provided for player """
        if foods_list != None:
            self.foods_list: list[Food] = [food for food in foods_list if isinstance(food, Food)]
        elif self.get_traders() != None:
            self.foods_list: list[Food] = []
        else:
            self.foods_list = foods_list
            
    def get_foods(self) -> list[Food]:
        """ Get the list of foods as an option for player """
        return self.foods_list     
    
    # caves
    def set_caves(self, caves_list: list[Cave] = None) -> None:
        """ Set the list of caves that is provided for player """
        self.caves_list = caves_list

    def get_caves(self) -> list[Cave]:
        """ Get the list of caves"""
        return self.caves_list 

    # (SOLO) select_food_and_caves
    def select_food_and_caves(self, offered_food: Food = None) -> tuple[Food | None, float, list[tuple[Cave, float]]]: 
        """
        
        Returns :
            tuple: _description_

        Approaches:
        SOLO food:
            Returns the food that has the most hunger filling while the balance is above 0

        SOLO caves:
            Returns caves in order of mining based on how much profit you can make from them

        SOLO Complexity: (best & worst) = O(T + F + C)


        MULTIPLAYER food:
            If the player can afford the food, they buy it. O(1)

        MULTIPLAYER caves:
            As you can only choose one cave, you want the most amount of profit possible from a single cave

        MULTIPLAYER Complexity: (best & worst) = O(C + T)
        """
        self.generate_material_price_map() # O(T)

        # if the offered food only one
        # refers to multiplayer gameplay
        if isinstance(offered_food, Food):
            if self.AI:
                chosen_food, chosen_caves = self.multiplayer_AI_select_food_and_caves(offered_food) # O(C)
            else:
                chosen_food, chosen_caves = self.get_multiplayer_real_player_choices(offered_food) # O(C)

        # singleplayer
        else:
            if self.AI:
                chosen_food, chosen_caves = self.AI_select_food_and_caves() #O(F+C)
            else:
                chosen_food, chosen_caves = self.get_solo_real_player_choices() #O(F+C)
    
        return (chosen_food, self.get_balance(), chosen_caves)
    
    def AI_select_food_and_caves(self) -> tuple[Food, list[Cave]]:
        """ Choose the food and caves if AI mode is True for solo gameplay """
        chosen_food = self.choose_food() #O(F)
        chosen_caves = self.choose_caves() #O(C)
        return chosen_food, chosen_caves
    
    def multiplayer_AI_select_food_and_caves(self, offered_food) -> tuple[Food|None, Cave]:
        """ Choose the food and caves if AI mode is True and in multiplayer mode game """
        chosen_food = self.multiplayer_choose_food(offered_food) #O(1)
        chosen_cave = self.multiplayer_choose_caves()
        return chosen_food, chosen_cave #O(C)
    
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
        if offered_food.price > self.get_balance():
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
        for cave in self.get_caves():
            try:
                quantity = cave.get_quantity_given_energy_spent(self.get_hunger())
                profit = self.get_material_price(cave.get_material())*quantity
            except KeyError:
                profit = 0
            if profit > max_profit:
                chosen_cave = cave
        return chosen_cave
    
    # helper methods
    
    def get_material_price(self, material: Material) -> float:
        """ Get the price of that particular material """
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
    
    
    
    
    # MANUAL CONTROL OF PLAYERS
    
    # SOLO 
    
    def get_solo_real_player_choices(self):
        """ Get the choice from player in singleplayer mode
        """
        while True:
            try:
                try:
                    chosen_food = self.choose_food_screen()
                except AssertionError:
                    chosen_food = None
                chosen_caves = self.choose_cave_screen()
                break
            except AssertionError:
                pass
            except Exception as e:
                raise e
            
            
    def choose_food_screen(self):
        """ UI to choose the food """
        raise NotImplementedError
        clearConsole()
        self.title = 'Food'
        foods = FOOD_NAMES  
        dark = '\033[90m'
        clear = '\033[0m'
        choice = 0
        
        
    def choose_cave_screen(self):
        """ UI to choose the cave """
        raise NotImplementedError
        clearConsole()
        self.title = 'Caves'
        caves = CAVE_NAMES  
        dark = '\033[90m'
        clear = '\033[0m'
        choice = 0
        
    
    # MULTI
    def get_multiplayer_real_player_choices(self, offered_food: Food):
        """ Ask input from user in multiplayer mode
        """
        while True:
            try:
                try:
                    chosen_food = self.multiplayer_choose_food_screen(offered_food)
                except AssertionError:
                    chosen_food = None
                chosen_caves = self.multiplayer_choose_cave_screen()
                break
            except AssertionError:
                pass
            except Exception as e:
                raise e 
    
    def multiplayer_choose_food_screen(self, offered_food):
        """ UI to show the food option in multiplayer mode """
        raise NotImplementedError
        clearConsole()
        self.title = 'Food'
        dark = '\033[90m'
        clear = '\033[0m'
        choice = 0
       
        
    def multiplayer_choose_cave_screen(self):
        """ UI to show the cave option in multiplayer mode
        """
        raise NotImplementedError
        clearConsole()
        self.title = 'Caves'
        caves = CAVE_NAMES  
        dark = '\033[90m'
        clear = '\033[0m'
        choice = 0
        
    
    # SOLO + MULTI METHODS
    
    def display_title(self):
        """ UI to show the title of the game """
        while True:
            try:
                title = self.title
                break
            except Exception as e:
                self.title = f"{e}"
        #
        screensize = get_screensize()
        big_text_len = len(big_text_print(title, 1))
        title_white_space = ' '*(screensize//2-(big_text_len//2)-1)
        #
        print(
f"""{title_white_space}{big_text_print(title, 1)}
{title_white_space}{big_text_print(title, 2)}
{title_white_space}{big_text_print(title, 3)}
{title_white_space}{big_text_print(title, 4)}
{title_white_space}{big_text_print(title, 5)}   
{'-'*screensize}
""")



if __name__ == "__main__":
    player = Player("Alex", emeralds=1000)
    player.display_title()
