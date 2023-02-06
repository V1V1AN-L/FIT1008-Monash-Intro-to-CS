from __future__ import annotations
from cave import *
from material import *
from food import *
from trader import Trader
from hash_table import *
from merge_sort import *

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


class Player:
    """
    NOTE: unless specified all methods have best and worst case complexity of O(1)

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

    MIN_EMERALDS = 20
    MAX_EMERALDS = 100

    def __init__(self, name, emeralds=None) -> None:
        """ Initialization """
        self.name = name
        self.set_balance(self.DEFAULT_EMERALDS if emeralds == None else emeralds)
        self.set_hunger()
        self.set_traders()
        self.set_foods()
        self.set_caves()

    def __str__(self) -> str:
        """ Formatted string representation """
        return f"{self.name}: {self.get_balance()}💰"

    def __repr__(self):
        """ Formatted string representation """
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
            self.hunger = round(hunger, 4)
        else:
            self.hunger = hunger

    def get_hunger(self) -> float:
        """ Get the hunger value of the player """
        self.set_hunger(self.hunger)  # makes sure it's rounded to two decimal places
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
        """ Rounding the emerald balance of the player by 4 number behind the decimal """
        self.balance = round(balance, 4)

    def get_balance(self) -> float:
        """ Get the emerald balance of the player"""
        self.set_balance(self.balance)  # makes sure its rounded to 4 decimal places
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
        if foods_list is not None:
            self.foods_list: list[Food] = [food for food in foods_list if isinstance(food, Food)]
        elif self.get_traders() is not None:
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
        self.generate_material_price_map()  # O(T)

        # if the offered food only one
        # refers to multiplayer gameplay
        if isinstance(offered_food, Food):
            chosen_food, expected_balance, chosen_caves = self.multiplayer_select_food_and_caves(offered_food)
        else:
            chosen_food, expected_balance, chosen_caves = self.solo_select_food_and_caves()

        return (chosen_food, expected_balance, chosen_caves)

    def solo_select_food_and_caves(self) -> tuple[Food, list[Cave]]:
        """
        Select the food and caves for solo player
        Complexity: O(C) but in this case, C is the chosen caves that is chosen by the player
        """
        expected_balance = self.get_balance()
        # food
        chosen_food = self.choose_food()
        if isinstance(chosen_food, Food):
            expected_balance -= chosen_food.price
            projected_hunger = chosen_food.hunger_bars
        else:
            projected_hunger = 0
        print(f'FOOD BALANCE: {expected_balance}')
        # caves
        chosen_caves = self.choose_caves()
        cave_profit = 0
        for cave in chosen_caves:
            quantity = cave.get_quantity_given_energy_spent(projected_hunger)
            profit = self.get_material_price(cave.get_material()) * quantity
        
        expected_balance += cave_profit
        
        
        # getting expected balance and printing out shit
        
        #for cave in chosen_caves:
        #    quantity = cave.get_quantity_given_energy_spent(total_hunger)
        #    profit_made = round(self.get_material_price(cave.get_material()) * cave.get_quantity(), 8)
        #    print(f'hunger before::::{self.hunger}')
        #    print(f'hunger TAKEN::::{round(cave.get_material().mining_rate * cave.get_quantity(), 8)}')
        #    hunger_taken = round(cave.get_material().mining_rate * cave.get_quantity(), 8)
        #    total_hunger -= hunger_taken
        #    print(f'hunger after::::{self.hunger}')
        #
        #    if total_hunger > 0:
        #        expected_balance += profit_made
        #        print(f'Profit made:::{profit_made}')
        #        print(f'BALANCE NOW:::{expected_balance}')
        #    else:
        #        quantity = round((hunger_taken + self.hunger) / cave.get_material().mining_rate, 8)
        #        total_hunger = 0
        #        expected_balance += round(self.get_material_price(cave.get_material()) * quantity, 8)
        #        print(f'Profit made:::{round(self.get_material_price(cave.get_material()) * quantity, 8)}')
        #        print(f'BALANCE NOW:::{expected_balance}')

        return chosen_food, expected_balance, chosen_caves

    def multiplayer_select_food_and_caves(self, offered_food) -> tuple[Food|None, Cave]:
        """
        Multiplayer mode, choose the food and the caves

        @see multiplayer_choose_caves()
        Complexity : O(C)
        """
        expected_balance = self.get_balance()
        chosen_food = self.multiplayer_choose_food(offered_food)
        if isinstance(chosen_food, Food):
            expected_balance -= chosen_food.price   
        chosen_cave = self.multiplayer_choose_caves(chosen_food)
        cave, quantity = chosen_cave
        if isinstance(cave, Cave) and quantity > 0:
            expected_balance += self.get_material_price(cave.get_material()) * quantity
            
        return chosen_food, expected_balance, chosen_cave  # O(C)

    # SOLO

    def choose_food(self) -> Food:
        """
        Choose the food

        Returns:
            Food: chosen food

        COMPLEXITY (best & worst) = O(F)
        """

        # food_dic = LinearProbeTable(len(self.get_foods()))
        # unit_price_lst = []
        # for food in self.get_foods():
        #     print(f'food price is::{food.price}')
        #     print(f'food huNGER is::{food.hunger_bars}')
        #
        #     if food.price<= self.balance:
        #         unit_price = food.hunger_bars / food.price
        #         food_dic.insert(str(round(unit_price,4)), food)
        #         unit_price_lst.append(round(unit_price,4))
        # print(f'FOODDDD UNIT PRICE LIST = {unit_price_lst}')
        #
        # unit_price_lst = msort(unit_price_lst)
        # food_choice = food_dic[str(unit_price_lst[len(unit_price_lst) - 1])]
        # # if self.balance< food_choice.price:
        # #     food_choice = food_dic[str(unit_price_lst[len(unit_price_lst) - 2])]
        # self.set_hunger(food_choice.hunger_bars)
        # self.balance -= food_choice.price
        # print(f'FOOD CHOICE: {food_choice}')
        #
        # return food_choice
        dic = {}
        res = []
        sort_based_on_hunger = []
        for food in self.get_foods():
            print(f'food price is::{food.price}')
            print(f'food huNGER is::{food.hunger_bars}')

            if food.price <= self.get_balance():
                res.append(food)
                sort_based_on_hunger.append(food.hunger_bars)
                dic.__setitem__(food.hunger_bars, food)
        if res is not None:
            sort_based_on_hunger.sort()
            food_choice = dic[sort_based_on_hunger[-1]]
            return food_choice
        else:
            return None

    def choose_caves(self) -> list[Cave]:
        """
        Choose the caves with the best output

        Returns:
            list[Cave]: list of caves in order of mining to

        Returns the caves in order of mining based on how much profit you can make from them

        COMPLEXITY COMPLEXITY (best & worst) = O(C)
        """

        cave_dic = LinearProbeTable(len(self.get_caves()))

        unit_price_lst = []
        cave_after_sort = []
        for cave in self.get_caves():  # (C)
            if self.get_material_price(cave.get_material()) != 0:
                unit_price = self.get_material_price(cave.get_material()) / cave.get_material().mining_rate
                print(
                    f'Material:{cave.get_material().name} :::Mining rate is::{cave.get_material().mining_rate} Price:::{self.get_material_price(cave.get_material())}')
                unit_price += cave.get_quantity() / 1000
                cave_dic.insert(str(round(unit_price, 8)), cave)
                unit_price_lst.append(round(unit_price, 8))

        unit_price_lst = msort(unit_price_lst)
        print(f'UNIT PRICE LIST = {unit_price_lst}')
        for j in unit_price_lst[::-1]:
            cave_after_sort.append(cave_dic[str(j)])

        player_hunger_spent = 0
        res = []
        for i in cave_after_sort:
            if player_hunger_spent <= self.get_hunger():
                player_hunger_spent += i.get_material().mining_rate * i.get_quantity()
                res.append(i)
            else:
                break
        return res

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

    def multiplayer_choose_caves(self, chosen_food) -> tuple[Cave, float]:
        """
        Choose 1 cave for each player

        Returns:
            the chosen caves for each player and the quantity that can be mined

        COMPLEXITY (best & worst) = O(C)
        """
        chosen_cave = None
        max_profit = 0
        chosen_quantity = 0
        projected_hunger = 0
        if isinstance(chosen_food, Food):
            projected_hunger = chosen_food.hunger_bars
        for cave in self.get_caves():
            quantity = cave.get_quantity_given_energy_spent(projected_hunger)
            profit = self.get_material_price(cave.get_material()) * quantity
            if profit >= max_profit:
                chosen_quantity = quantity
                chosen_cave = cave
                max_profit = profit
        return (chosen_cave, float(chosen_quantity))

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

        COMPLEXITY (best & worst) = O(T), T = amount of traders available to trade
        """
        # material_map = LinearProbeTable(len(self.get_traders()))
        material_map = {}
        for trader in self.get_traders():
            try:
                material, selling_price = trader.current_deal()
                if material_map.__contains__(f"{material}") and selling_price < material_map.__getitem__(f"{material}"):
                    break
                else:
                    material_map[f"{material}"] = selling_price
            except ValueError:
                pass

        self.material_price_map = material_map
        return self.material_price_map
