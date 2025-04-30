import time
import colorama
import Team
import Arena
import UnitClases
import Shop

class Game():
    player_name = None
    player_gold = 1000
    all_arenas = 5
    arena_counter = 0
    player_team = None
    shop = None
    game_result = None

    def start_board(self):
        print(colorama.Fore.RED + f'''
        ---------------------------------------------------------------------------------------------------------------------------------------------
        **************************************************************************** Heroes Game*****************************************************
        
                                                                                b m w h
        
        ---------------------------------------------------------------------------------------------------------------------------------------------''')
        self.player_name = input("Type you name, Player ---> ")
        time.sleep(1)
        print(f'''
    Welcome,player {self.player_name}!
    Here is you money{self.player_gold} to begin to you {self.all_arenas}
    Let's play the game!
        ''')
        time.sleep(0)
        self.player_team = Team.Team()
        start_team = [UnitClases.Knight(),
                      UnitClases.Healer(),
                      UnitClases.Catapult(),
                      UnitClases.Archer()]
        self.player_team.team.extend(start_team)

        print(f'''
You have squad with 4 units
All you units special.
Lets go to the shop and buy some units

Goodbay''')

    def final_winner_board(self):
        pass

    def final_looser_board(self):
        pass

    def up_team(self):
         pass

    def start_game(self):
        self.start_board()
        while self.arena_counter < self.all_arenas:
            shop = Shop.Shop(self.player_team, self.player_gold)
            game_after_shop = shop.welcome_board()
            if game_after_shop == False:
                self.game_result = False
                break
            arena = Arena.Arena(self.player_team,self.arena_counter)
            arena.start_arena()

            if len(self.player_team.alive_team) == 0:
                self.game_result = False
                break

            self.arena_counter += 1
            self.up_team()
        if self.game_result == True:
            self.final_winner_board()
        elif self.game_result == False:
            self.final_looser_board()

game = Game()
game.start_game()