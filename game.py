from __future__ import annotations

from player import *
from trader import Trader
from material import Material
from cave import Cave
from food import Food
from random_gen import RandomGen


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

    def initialise_game(self, print_data: bool = True) -> None:
        """Initialise all game objects: Materials, Caves, Traders."""
        N_MATERIALS = RandomGen.randint(self.MIN_MATERIALS, self.MAX_MATERIALS)
        self.generate_random_materials(N_MATERIALS)
        N_CAVES = RandomGen.randint(self.MIN_CAVES, self.MAX_CAVES)
        self.generate_random_caves(N_CAVES)
        N_TRADERS = RandomGen.randint(self.MIN_TRADERS, self.MAX_TRADERS)
        self.generate_random_traders(N_TRADERS)
        if print_data:
            print("Materials:\n\t", end="")
            print("\n\t".join(map(str, self.get_materials())))
            print("Caves:\n\t", end="")
            print("\n\t".join(map(str, self.get_caves())))
            print("Traders:\n\t", end="")
            print("\n\t".join(map(str, self.get_traders())))

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], print_data: bool = True):
        self.set_materials(materials)
        self.set_caves(caves)
        self.set_traders(traders)
        if print_data:
            print("Materials:\n\t", end="")
            print("\n\t".join(map(str, self.get_materials())))
            print("Caves:\n\t", end="")
            print("\n\t".join(map(str, self.get_caves())))
            print("Traders:\n\t", end="")
            print("\n\t".join(map(str, self.get_traders())))

    def set_materials(self, mats: list[Material] = None) -> None:
        self.materials = mats
        self.material_price_map: dict = None

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
        materials = []
        while len(materials) < amount:
            material = Material.random_material()
            name = [each.name for each in materials]
            if material.name not in name:
                materials.append(material)
        self.set_materials(materials)

    def generate_random_caves(self, amount):
        """
        Generates <amount> random caves using Cave.random_cave
        Generated caves must all have different names
        (You may have to call Cave.random_cave more than <amount> times.)
        """
        caves = []
        while len(caves) < amount:
            cave = Cave.random_cave(self.get_materials())
            name = [each.name for each in caves]
            if cave.name not in name:
                caves.append(cave)
        self.set_caves(caves)

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
        material_map = LinearProbeTable(len(self.get_traders()))
        for trader in self.get_traders():
            try:
                material, selling_price = trader.current_deal()
                material_map[f"{material}"] = selling_price
            except ValueError:
                pass
            
        
        self.material_price_map = material_map
        return self.material_price_map
            
    # can be used in both SOLO games and MULTIPLAYER games
    def calculate_hunger_emerald_material_changes(self, player: Player, cave: Cave, mined_quantity: float = None) -> None:
        """ 
        Given a player, cave, and the quantity mined, changes the player's hunger and emerald balance, while also
        reducing the remaining material count in the cave.
        """
        if isinstance(cave, Cave):
            selling_rate = self.get_material_price(cave.get_material())

            if mined_quantity == None:
                mined_quantity = cave.get_quantity_given_energy_spent(player.get_hunger())
                if mined_quantity == 0:
                    return cave
                
            player.decrease_hunger(cave.calculate_total_hunger_spent(mined_quantity))  
    
            player.increase_balance(mined_quantity*selling_rate) 
            cave.remove_quantity(mined_quantity)    

            player.check_hunger()
            
        return cave


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

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float], print_data: bool = True):
        super().initialise_with_data(materials, caves, traders, print_data)
        self.player: Player = Player(player_names[0], emeralds=emerald_info[0])
        self.player.set_materials(self.get_materials())
        self.player.set_caves(self.get_caves())
        self.player.set_traders(self.get_traders())

    def simulate_day(self, print_data: bool = True):
        # 1. Traders make deals
        self.generate_trader_deals()
        self.player.set_traders(self.get_traders())
        if print_data:
            print("Traders Deals:\n\t", end="")
            print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        foods = self.generate_food()
        self.player.set_foods(foods)
        if print_data:
            print("\nFoods:\n\t", end="")
            print("\n\t".join(map(str, foods)))
        # 3. Select one food item to purchase
        food, balance, caves = self.player.select_food_and_caves()
        if print_data:
            print(f"{self.player} | Chosen Food: {food} | Chosen Caves: {caves}")
        # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(food, balance, caves)

    def verify_output_and_update_quantities(self, food: Food, balance: float, caves: list[
        Cave]):  # (self, food: Food | None, balance: float, caves: list[tuple[Cave, float]]) -> None:
        """
        verifies the result of a round of gameplay is consistent with expected values
        raises an error if expectations are not met

        the results verified and updated are:
        Player emerald balance
        Player hunger levels
        cave material quantity

        """
        # ensure emerald balance is sufficent to purchase food
        if isinstance(food, Food):
            assert balance > food.price
        assert balance > 0

        # update emerald balance
        if isinstance(food, Food):
            self.player.decrease_balance(food.price)
        assert self.player.get_balance() >= 0

        # update hunger levels
        if isinstance(food, Food):
            self.player.set_hunger(food.hunger_bars)
        else:
            self.player.set_hunger(0)
        # verify hunger > 0
        assert self.player.get_hunger() >= 0

        # map all materials to a price
        self.material_price_map = self.generate_material_price_map()

        # add emeralds and update hunger and update quantites for caves
        for i, cave in enumerate(caves):
            caves[i] = self.calculate_hunger_emerald_material_changes(self.player, cave)

        # updates the quantities
        self.player.clear_hunger()
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

    def initialise_game(self, print_data: bool = True) -> None:
        super().initialise_game(print_data)
        N_PLAYERS = RandomGen.randint(self.MIN_PLAYERS, self.MAX_PLAYERS)
        self.generate_random_players(N_PLAYERS)
        for player in self.players:
            player.set_materials(self.get_materials())
            player.set_caves(self.get_caves())
            player.set_traders(self.get_traders())
        if print_data:
            print("Players:\n\t", end="")
            print("\n\t".join(map(str, self.players)))

    def generate_random_players(self, amount) -> None:
        """Generate <amount> random players. Don't need anything unique, but you can do so if you'd like."""
        raise NotImplementedError()

    def initialise_with_data(self, materials: list[Material], caves: list[Cave], traders: list[Trader], player_names: list[int], emerald_info: list[float], print_data: bool = True):
        super().initialise_with_data(materials, caves, traders, print_data)
        for player, emerald in zip(player_names, emerald_info):
            self.players.append(Player(player, emeralds=emerald))
            self.players[-1].set_materials(self.get_materials())
            self.players[-1].set_caves(self.get_caves())
            self.players[-1].set_traders(self.get_traders())
        if print_data:
            print("Players:\n\t", end="")
            print("\n\t".join(map(str, self.players)))

    def simulate_day(self, print_data: bool = True):
        # 1. Traders make deals
        self.generate_trader_deals()
        for i in range(len(self.players)):
            self.players[i].set_traders(self.get_traders())
        if print_data:
            print("Traders Deals:\n\t", end="")
            print("\n\t".join(map(str, self.get_traders())))
        # 2. Food is offered
        offered_food = Food.random_food()
        if print_data:
            print(f"\nFoods:\n\t{offered_food}")
        # 3. Each player selects a cave - The game does this instead.
        foods, balances, caves = self.select_for_players(offered_food)
        if print_data:
            for i in range(len(self.players)):
                print(f"{self.players[i]} | Chosen Food: {foods[i]} | Chosen Caves: {caves[i][0]}")
        # 4. Quantites for caves is updated, some more stuff is added.
        self.verify_output_and_update_quantities(foods, balances, caves)

    def select_for_players(self, offered_food: Food) -> tuple[
        list[Food | None], list[float], list[tuple[Cave, float] | None]]:
        """_summary_

Complexity Requirement!
Given that M=#Materials, T=#Traders, C=#Caves, P=#Players,
the select_for_players method should have complexity at most O(M + T + C + P * log C).

Documentation Requirement!
For your solution to select_for_players, please leave a lengthy docstring describing the motivation for your approach in full.
Please use a small example to demonstrate your approach. Additionally, you need to fully justify the complexity of your approach - Give line comments to summarise the complexity of blocks of your code.

Motivation:



        """
        foods = []
        balances = []
        caves = []
        for i in range(len(self.players)):
            food, balance, cave_tuple = self.players[i].select_food_and_caves(offered_food)
            foods.append(food)
            balances.append(balance)
            caves.append(cave_tuple)
            # update the quantities in game so that other players quantities will be updated (only players that need the quantities updated)
            self.update_cave_quantity(cave_tuple)
            for j in range(i, len(self.players)):
                self.players[j].set_caves(self.get_caves())
            
        return foods, balances, caves

    def verify_output_and_update_quantities(self, foods: list[Food | None], balances: list[float], caves: list[tuple[Cave, float] | None]) -> None:
        self.generate_material_price_map()
        # modify other players lists so that mining happens real time

        for i in range(len(self.players)):
            # ensure emerald balance is sufficent to purchase food
            food = foods[i]
            balance = balances[i]
            cave, amount_of_material_mined = caves[i]
            if isinstance(food, Food):
                assert balance >= food.price, f"{self.players[i]} {balance} should be >= {food.price}"
                # update emerald balance
                self.players[i].decrease_balance(food.price)
                # update hunger levels
                self.players[i].set_hunger(food.hunger_bars)
            else:
                assert balance >= 0, f"{self.players[i]} balance is {balance} when it is supposed to be >= 0"

            

            # verify hunger >= amount mined
            if isinstance(cave, Cave):
                assert self.players[i].get_hunger() >= cave.calculate_total_hunger_spent(amount_of_material_mined), f"{self.players[i]} {self.players[i].get_hunger()} >!= {cave.calculate_total_hunger_spent(amount_of_material_mined)}"
            else:
                assert self.players[i].get_hunger() >= 0, f"{self.players[i]} should be reset to 0 at the end of every turn"
            
            # add emeralds and update hunger and update quantites for caves
            self.calculate_hunger_emerald_material_changes(self.players[i], cave, amount_of_material_mined)

            # updates the quantities
            self.players[i].set_caves(self.get_caves())  # updates all players caves
            self.players[i].clear_hunger()

    # helper functions

    def update_cave_quantity(self, chosen_cave_tuple: list[Cave, float]):
        chosen_cave, amount_mined = chosen_cave_tuple
        if isinstance(chosen_cave, Cave):
            caves_list = self.get_caves()
            for i in range(len(caves_list)):
                if caves_list[i] == chosen_cave:
                    caves_list[i].remove_quantity(amount_mined)
                    break
            self.set_caves(caves_list)
                
            
            

if __name__ == "__main__":
    r = RandomGen.seed  # Change this to set a fixed seed.
    RandomGen.set_seed(r)
    print(r)

    g = SoloGame()
    g.initialise_game()

    g.simulate_day()
    g.finish_day()

    g.simulate_day()
    g.finish_day()
