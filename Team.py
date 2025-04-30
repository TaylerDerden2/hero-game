import random
import UnitClases

class Team:
    alive_team = property()
    dead_team = property()


    def __init__(self,init_name = "NoName",init_team = []):
        self.name = init_name
        self.team = init_team

    @alive_team.getter
    def alive_team(self):
        result = []
        for u in self.team:
            if u.status == "alive":
                result.append(u)
        return result

    @dead_team.getter
    def dead_team(self):
        result = []
        for u in self.team:
            if u.status == "dead":
                result.append(u)
        return result

    def chose_unit_by_player(self):
        unit = None
        while True:
            x = input("Введи індекс ходяче сало🐷 - ")

            try:
                unit = self.team[int(x)]
                break
            except:
                print("Введіть нормально")
                continue
        return unit

    def team_info(self, chosing = False):
        print(f'''
        ------------------    
            {self.name}
        ------------------      
        ''')
        if len(self.dead_team) == 0:
            for u in self.alive_team:
                if chosing == True:
                    print(self.alive_team.index(u), end = ") ")
                u.unit_info()
        elif len(self.alive_team) == 0:
            print("ALL UNITS DIE")
            for u in self.dead_team:
                u.unit_info()
        else:
            print("ALIVE:")
            for u in self.alive_team:
                if chosing == True:
                    print(self.alive_team.index(u), end = ") ")
                u.unit_info()
            print()
            print("DEAD:")
            for u in self.dead_team:
                u.unit_info()
            print()
        return

    def create_rand_comp_team(self):
        all_names = ["Monser's Squad👾",
                     "Chinchilla team🐭",
                     "Scibidi toilets🚽💩",
                     "Cameramans",
                     "Jokers",
                     "Ricrroll Team",
                     "Dogs and Cats🐶🐺",
                     "Fake chinchillas",
                     "Бетмен",
                     "Дід Пихто та баба з пісталетом"]
        self.name = random.choice(all_names)





        all_units = [UnitClases.Archer,
                     UnitClases.Catapult,
                     UnitClases.Wizard,
                     UnitClases.Defender,
                     UnitClases.Healer,
                     UnitClases.Knight]
        for i in range(0):
            self.team.append(random.choice(all_units)())

    def chose_random_unit(self):
        return random.choice(self.alive_team)