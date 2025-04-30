import Team
import time
import Fight


class Arena():
    def __init__(self,init_p_team,init_arena_counter):
        self.player_team = init_p_team
        self.arena_counter = init_arena_counter
        self.comp_team = Team.Team()

    def start_arena(self):
        self.comp_team.create_rand_comp_team()
        self.upgrade_comp_team_by_arena_counter()
        time.sleep(1)
        self.arena_set_health()
        time.sleep(1)
        self.arena_start_board()
        self.arena_fight()
        self.arena_final_board()
        self.arena_lvl_up()

    def upgrade_comp_team_by_arena_counter(self):
        pass
        #доробете прокачку
        for unit in self.comp_team.team:
            if self.arena_counter == 1:
                pass
            if self.arena_counter == 2:
                pass
    def arena_lvl_up(self):
        for unit in self.player_team.alive_team:
            unit.health_default *= 1.2

            #доробити левеле упе для всіх рабів нашої команди

    def arena_set_health(self):
        for team in [self.player_team.team,self.comp_team.team]:
            for unit in team:
                unit.health_in_fight = unit.health_with_armor

    def arena_final_board(self):
        print(f'''
            ----------------------------------------------------
                ***** Arena #{self.arena_counter} Final Board ********
            ----------------------------------------------------
                        Goodbay!
            {self.player_team.name}            ⚔            {self.comp_team.name}

            ''')

        if len(self.player_team.alive_team) ==0 and len(self.comp_team.alive_team) ==0:
            winner = None
        elif len(self.player_team.alive_team) !=0:
            winner = self.player_team
        else:
            winner = self.comp_team
        if not winner:
            print(f"DRAW")
        else:
            print(f"The winner of #{self.arena_counter} Arena is: {winner.name}")

            print(f"Alive units of {winner.name} squad")

            print()

            ''
            print(f"Dead units of {winner.name} squad:")
            winner.dead_team.team_info()
        print("")
    def arena_start_board(self):

        print(f'''
    ----------------------------------------------------
        ***** Arena #{self.arena_counter} Board ********
    ----------------------------------------------------
                Welocome to the Arena!
    {self.player_team.name}            ⚔            {self.comp_team.name}
    {time.sleep(1)}
    ''')
        print("Player Team")
        self.player_team.team_info()

        print()
        print("Computer Team")
        self.comp_team.team_info()

    def arena_fight(self):
        time.sleep(1)
        fight_counter = 1

        while len(self.player_team.alive_team) !=0 and len(self.comp_team.alive_team) !=0 :

            if fight_counter % 2 != 0:
                time.sleep(2)
                print()
                print("PLayer chose your fighter!")
                self.player_team.team_info(True)
                player_unit = self.player_team.chose_unit_by_player()

                print()
                print("PLayer chose comp fighter!")
                self.comp_team.team_info(True)
                comp_unit = self.comp_team.chose_unit_by_player()
                fight_counter += 1
                continue
            else:
                print("Хід компа")
                comp_unit = self.comp_team.chose_random_unit()
                player_unit = self.player_team.chose_random_unit()

            time.sleep(1)

            fight = Fight.Fight(player_unit,comp_unit,fight_counter,self.player_team,self.comp_team)

            fight_counter += 1
            time.sleep(1)
