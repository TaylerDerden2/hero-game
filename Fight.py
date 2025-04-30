from email.quoprimime import header_length


class Fight():
    def __init__(self,init_player_unit,init_comp_unit,init_fight_counter,init_player_team,init_comp_team):
        self.player_unit = init_player_unit
        self.comp_unit = init_comp_unit
        self.fight_counter = init_fight_counter
        self.player_team = init_player_team
        self.comp_team = init_comp_team

        self.dispay_start_board()
        self.hitmaker()
        self.display_final_board()


    def fight_start(self):
        self.dispay_start_board()
        self.hitmaker()
        self.display_final_board()
    def dispay_start_board(self):
        print(f'''
        ------------------------------------------------
               ********* Fight № {self.fight_counter} *********  
        ------------------------------------------------
        Player                                  Computer
        {self.player_unit.name}                                  {self.comp_unit.name}
        
        Let's The fight begin!
        ''')
    def use_ability(self,unit,enemy,unit_team,enemy_team):

        unit.ability.cooldown_left = unit.ability.cooldown

        if unit.name == "Catapult":
            print(f"{unit.name} makes SUPER ATTACK!")
            hit = unit.ability.value * unit.attack_with_weapon
            enemy.health_in_fight -= hit
            print(f"{unit.name} hits {enemy.name} by {hit}")
        elif unit.name == "Healer":
            print(f"{unit.name} makes SUPER HEAL!")
            for u in unit_team.alive_team:
                heal = unit.ability.value * u.health_with_armor
                u.health += heal
                print(f"-------> {u.name} was healed by {heal}hp")
        elif unit.name == "Knight":
            print(f"{unit.name} makes SPLASH ATTACK")
            hit = unit.ability.value * unit.attack_with_weapon
            for u in enemy_team.alive_team:
                u.health_in_fight -= hit
                print(f"------->{unit.name} hits {u.name} by {hit}hp")
        elif unit.name == "Wizard":
            print(f"{unit.name} makes SUPER STONE!")
            for u in enemy_team.alive_team:
                u.stunned = True
                print(f"{u.name} was stunned!")
        elif unit.name == "Defender":
            print(f"{unit.name} makes SUPER SHIELD")
            for u in unit_team.alive_team:
                u.magic_shield = True
                print(f"------> {u.name} gets super shield")
        elif unit.name == "Archer":
            print(f"{unit.name} makes POISONED ARROWS")
            enemy.poisoned_moves = 3
            enemy.poisoned_damage = unit.ability.value
    def comp_check_abilities(self,comp_unit,comp_team,player_unit,player_team):
        if not comp_unit.ability.cooldown_left > 0:
            comp_unit.ability.cooldown_left -=1
        else:
            print(f"{comp_unit.name} uses its ability {comp_unit.ability.name} - {comp_unit.ability.description}")
            self.use_ability(comp_unit,player_unit,comp_team,player_team)
    def player_check_abilities(self,player_unit,comp_unit,player_team,comp_team):


        if  player_unit.ability.cooldown_left > 0:
            player_unit.ability.cooldown_left -= 1
        else:
            print(f"{comp_unit.name} has its ability {comp_unit.ability}")
            while True:
                answer = input("Do you want to use ability? (Y/N)")
                if not len(answer) or not answer.upper()[0]!="Y" not in ["Y","N"]:
                    continue
                elif answer.upper()[0] == "N":
                    return
                elif answer.upper()[0] == "y":
                    self.use_ability(player_unit,comp_unit,player_team,comp_team)
    def hitmaker(self):
        self.player_check_abilities(self.player_unit,self.comp_unit,self.player_team,self.comp_team)
        self.player_unit.hit(self.comp_unit)

        self.comp_check_abilities(self.player_unit,self.comp_unit,self.player_team,self.comp_team)
        self.comp_unit.hit(self.player_unit)


    def display_final_board(self):
        print()
        self.player_unit.unit_info()
        self.comp_unit.unit_info()
        print("-"*2999999999999999999999999999999999999999999989898989898899999999999999995)