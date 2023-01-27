from __future__ import annotations

from player import Player
from trader import Trader
from material import Material
from cave import Cave
from food import Food
from random_gen import RandomGen
import numpy

class Game:
    """
    NOTE: unless specified all methods have a best and worst case complexity of O(1)
    """

    MIN_MATERIALS = 5
    MAX_MATERIALS = 10

    MIN_CAVES = 5
    MAX_CAVES = 10

    MIN_TRADERS = 4
    MAX_TRADERS = 8

    MIN_FOOD = 2
    MAX_FOOD = 5

    def __init__(self) -> None:
        self.set_materials()
        self.set_caves()
        self.set_traders()

    def initialise_game(self) -> None:
        """Initialise all game objects: Materials, Caves, Traders."""
        N_MATERIALS = RandomGen.randint(self.MIN_MATERIALS, self.MAX_MATERIALS)
        self.generate_random_materials(N_MATERIALS)
        print("Materials:\n\t", end="")
        print("\n\t".join(map(str, self.get_materials())))
        N_CAVES = RandomGen.randint(self.MIN_CAVES, self.MAX_CAVES)
        self.generate_random_caves(N_CAVES)
        print("Caves:\n\t", end="")
        print("\n\t".join(map(str, self.get_caves())))
        N_TRADERS = RandomGen.randint(self.MIN_TRADERS, self.MAX_TRADERS)
        self.generate_random_traders(N_TRADERS)
        print("Traders:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader]):
        self.set_materials(materials)
        print("Materials:\n\t", end="")
        print("\n\t".join(map(str, self.get_materials())))
        self.set_caves(caves)
        print("Caves:\n\t", end="")
        print("\n\t".join(map(str, self.get_caves())))
        self.set_traders(traders)
        print("Traders:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))

    def set_materials(self, mats: list[Material] = None) -> None:
        self.materials = mats
        self.material_price_map: dict

    def set_caves(self, caves: list[Cave] = None) -> None:
        self.caves = caves

    def set_traders(self, traders: list[Trader] = None) -> None:
        self.traders = traders

    def get_materials(self) -> list[Material]:
        return self.materials 

    def get_caves(self) -> list[Cave]:
        return self.caves 

    def get_traders(self) -> list[Trader]:
        return self.traders 

    def generate_random_materials(self, amount):
        """
        Generates <amount> random materials using Material.random_material
        Generated materials must all have different names and different mining_rates.
        (You may have to call Material.random_material more than <amount> times.)
        """
        self.set_materials([Material.random_material() for _ in range(amount)])
        
    def generate_random_caves(self, amount):
        """
        Generates <amount> random caves using Cave.random_cave
        Generated caves must all have different names
        (You may have to call Cave.random_cave more than <amount> times.)
        """
        self.set_caves([Cave.random_cave(self.get_materials()) for _ in range(amount)])

    def generate_random_traders(self, amount):
        """
        Generates <amount> random traders by selecting a random trader class
        and then calling <TraderClass>.random_trader()
        and then calling set_all_materials with some subset of the already generated materials.
        Generated traders must all have different names
        (You may have to call <TraderClass>.random_trader() more than <amount> times.)
        """
        trader_list = []
        for i in range(amount):
            _trader = Trader.random_trader() 
            _trader.set_all_materials(self.get_materials())
            trader_list.append(_trader)
        self.set_traders(trader_list)

    def finish_day(self):
        """
        DO NOT CHANGE
        Affects test results.
        """
        for cave in self.get_caves():
            if cave.quantity > 0 and RandomGen.random_chance(0.2):
                cave.remove_quantity(RandomGen.random_float() * cave.quantity)
            else:
                cave.add_quantity(round(RandomGen.random_float() * 10, 2))
            cave.quantity = round(cave.quantity, 2)
            
    # user defined helper methods
    
    def generate_trader_deals(self):
        """_summary_
        """
        for trader in self.get_traders():
            trader.generate_deal()
            
    # can be used in both SOLO games and MULTIPLAYER games
    def calculate_hunger_emerald_material_changes(self, player: Player, cave: Cave) -> None:
        """
        given a player and cave, changes the player's hunger and emerald balance, while
        reducing the material count in the cave
        """
        selling_rate = self.material_price_map[cave.get_material()]
        player.decrease_hunger(cave.calculate_total_hunger_spent())  
        if player.get_hunger() > 0:
            player.increase_balance(cave.get_quantity()*selling_rate)
            cave.clear_quantity()

        else: # determine max amount mined with remaining hunger
            mined_quantity = numpy.linalg.solve(cave.material.mining_rate, player.get_hunger())
            player.clear_hunger()
            player.increase_balance(mined_quantity*selling_rate) 
            cave.remove_quantity(mined_quantity)    

        return cave
    
    def generate_material_price_map(self):
        trader_list = self.get_traders()
        material_map = {}
        for trader in trader_list:
            material, selling_price = trader.current_deal()
            material_map[material] = selling_price
            
        self.material_price_map = material_map


class SoloGame(Game):
    
    def __init__(self) -> None:
        super().__init__()
        self.player: Player = None

    def initialise_game(self) -> None:
        super().initialise_game()
        self.player: Player = Player.random_player()
        self.player.set_materials(self.get_materials())
        self.player.set_caves(self.get_caves())
        self.player.set_traders(self.get_traders())

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float]):
        super().initialise_with_data(materials, caves, traders)
        self.player: Player = Player(player_names[0], emeralds=emerald_info[0])
        self.player.set_materials(self.get_materials())
        self.player.set_caves(self.get_caves())
        self.player.set_traders(self.get_traders())

    def simulate_day(self):
        # 1. Traders make deals
        self.generate_trader_deals()
        print("Traders Deals:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        foods = self.generate_food()
        self.player.set_foods(foods)
        print("\nFoods:\n\t", end="")
        print("\n\t".join(map(str, foods)))
        # 3. Select one food item to purchase
        food, balance, caves = self.player.select_food_and_caves()
        print(f"{self.player} | Chosen Food: {food} | Chosen Caves: {caves}")
        # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(food, balance, caves)

    def verify_output_and_update_quantities(self, food: Food, balance: float, caves: list[Cave]):    #(self, food: Food | None, balance: float, caves: list[tuple[Cave, float]]) -> None:
        """
        verifies the result of a round of gameplay is consistent with expected values
        raises an error if expectations are not met

        the results verified and updated are:
        Player emerald balance
        Player hunger levels
        cave material quantity

        """
        #### Not Finished #### i misread the damn task, so this method does the incorrect thing
        # ensure emerald balance is sufficent to purchase food
        assert balance > food.price

        # update emerald balance
        self.player.set_balance(balance - food.price)
        # update hunger levels
        self.player.set_hunger(food.hunger_bars) # will hunger from previous day carry over?

        # verify hunger > 0
        assert self.player.get_hunger > 0
        
        # map all materials to a price
        self.material_price_map = self.generate_material_price_map()

        # add emeralds and update hunger and update quantites for caves
        for i, cave in enumerate(caves):
            caves[i] = self.calculate_hunger_emerald_material_changes(self.player, cave)
            
        # updates the quantities
        self.set_caves(caves)

    
    # user defined helper methods
    
    def generate_food(self):
        food_num = RandomGen.randint(self.MIN_FOOD, self.MAX_FOOD)
        foods = []
        for _ in range(food_num):
            foods.append(Food.random_food())
        self.player.set_foods(foods)
        return foods
    
    
    
    
    
    
    

class MultiplayerGame(Game):

    MIN_PLAYERS = 2
    MAX_PLAYERS = 5

    def __init__(self) -> None:
        super().__init__()
        self.players: list[Player] = []

    def initialise_game(self) -> None:
        super().initialise_game()
        N_PLAYERS = RandomGen.randint(self.MIN_PLAYERS, self.MAX_PLAYERS)
        self.generate_random_players(N_PLAYERS)
        for player in self.players:
            player.set_materials(self.get_materials())
            player.set_caves(self.get_caves())
            player.set_traders(self.get_traders())
        print("Players:\n\t", end="")
        print("\n\t".join(map(str, self.players)))

    def generate_random_players(self, amount) -> None:
        """Generate <amount> random players. Don't need anything unique, but you can do so if you'd like."""
        raise NotImplementedError()

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float]):
        super().initialise_with_data(materials, caves, traders)
        for player, emerald in zip(player_names, emerald_info):
            self.players.append(Player(player, emeralds=emerald))
            self.players[-1].set_materials(self.get_materials())
            self.players[-1].set_caves(self.get_caves())
            self.players[-1].set_traders(self.get_traders())
        print("Players:\n\t", end="")
        print("\n\t".join(map(str, self.players)))

    def simulate_day(self):
        # 1. Traders make deals
        self.generate_trader_deals()
        print("Traders Deals:\n\t", end="")
        print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        offered_food = Food.random_food()
        print(f"\nFoods:\n\t{offered_food}")
        # 3. Each player selects a cave - The game does this instead.
        foods, balances, caves = self.select_for_players(offered_food)
        for i in range(len(self.players)):
            print(f"{self.players[i]} | Chosen Food: {foods[i]} | Chosen Caves: {caves[i][0]}")
        # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(foods, balances, caves)

    def select_for_players(self, offered_food: Food) -> tuple[list[Food | None], list[float], list[tuple[Cave, float] | None]]:
        """_summary_

Complexity Requirement!
Given that M=#Materials, T=#Traders, C=#Caves, P=#Players, 
the select_for_players method should have complexity at most O(M + T + C + P * log C).

Documentation Requirement!
For your solution to select_for_players, please leave a lengthy docstring describing the motivation for your approach in full. 
Please use a small example to demonstrate your approach. Additionally, you need to fully justify the complexity of your approach - Give line comments to summarise the complexity of blocks of your code.

MOTIVATION (VIRGIL STATUS):
        """
        foods = []
        balances = []
        caves = []
        for player in self.players:
            food, balance, cave_tuple = player.select_food_and_caves(offered_food)
            foods.append(food)
            balances.append(balance)
            caves.append(cave_tuple)
            # modify other players lists so that mining happens real time
            
        return foods, balances, caves
            
            
    def verify_output_and_update_quantities(self, foods: list[Food | None], balances: list[float], caves: list[tuple[Cave, float]|None]) -> None:
        self.generate_material_price_map()

if __name__ == "__main__":

    r = RandomGen.seed # Change this to set a fixed seed.
    RandomGen.set_seed(r)
    print(r)

    g = SoloGame()
    g.initialise_game()

    g.simulate_day()
    g.finish_day()

    g.simulate_day()
    g.finish_day()
