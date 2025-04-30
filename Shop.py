import Team
import sqlite3
import colorama
import UnitClases


class Shop():
    def __init__(self,init_team,init_gold):
        self.team = init_team
        self.gold = init_gold


    def choose_unit(self):
        self.team.team_info()
        unit = None
        while not unit:
            answer = input("Choose unit to buy anything")
            try:
                answer = int(answer)
            except:
                continue
            if answer < 0 or answer > len(self.team.team) - 1:
                continue

            unit = self.team.team[answer]
            return unit

    def choose_item(self,data,unit_id):
        result = []
        for ar in data:
            if ar[1] == "ALL" or ar[1] == unit_id:
                result.append(ar)
        print(result)

        for x in range(len(result)):
            name = result[x][0]
            value = result[x][2]
            price = result[x][3]
            print(f"{x}) {name} - {value} value - {price} gold")
        item = None
        while not item:
            answer = input("Choose item to buy")
            try:
                answer = int(answer)
            except:
                continue
            if answer < 0 or answer > len(self.team.team) - 1:
                continue

            item = result[answer]
            return item



    def display_menu(self,list,menu_category):
        for i in range(len(list)):
            if menu_category == "item categories":
                print(f"{i}.{list[i][0]}")
            if menu_category == "units":
                name = list[i][0]
                price = list[i][1]
                print(f"{i}. {name}, {price} Gold")
            if menu_category == "armor":
                pass
            if menu_category == "weapons":
                pass
            if menu_category == "abilities":
                pass

        print(f"{len(list)}. Show you team to analize")
        print(f"{len(list)+1}. Return to previous page")


    def ask_answer(self,list):
        while True:
            answer = input("Chose category ->")

            try:
                answer = int(answer)
            except:
                continue
            if answer < 0 or answer > len(list)+1:
                continue
            if answer == len(list):
                self.team.team_info()
                continue
            return answer


    def check_gold_for_min_units(self):
        min_gold_to_have = 0
        db = sqlite3.connect("Shop_DB.db")
        agent_tosya = db.cursor()

        agent_tosya.execute("SELECT name, price FROM units")
        data = agent_tosya.fetchall()
        min_unit_price = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

        for unit in data:
            if unit[1] < min_unit_price:
                min_unit_name = unit[0]
                min_unit_price = unit[1]

        units_to_buy = (5-len(self.team.team))
        min_gold_to_have = min_unit_price * units_to_buy

        return min_gold_to_have, min_unit_name, units_to_buy


    def welcome_board(self):
        min_gold_to_have, min_unit_name, units_to_buy = self.check_gold_for_min_units()
        print(colorama.Fore.LIGHTBLUE_EX + f'''
        -----------------------------------------
                Welcome to the shop
        -----------------------------------------
        You have {self.gold} gold
        Please, choose you want to do in shop:
        0.See all categories
        1.Look at yours unit's
        2.Exit from shop
        ''')

        answer = None
        while answer not in ["0","1","2"]:
            answer = input("------> ")
            if answer not in ["0","1","2"]:
                continue

            if answer == "0":
                self.item_types()
                answer = None
                break

            if answer == "1":
                self.team.team_info()
                answer = None
                continue

            if answer == "2":
                if units_to_buy > 0 and self.gold > min_gold_to_have:
                    print(f'''You can't leave shop because you haven't got 5 units
                    You should by {units_to_buy}units.Cheapest is {min_unit_name}''')
                    answer = None
                    continue

                elif units_to_buy > 0 and self.gold < min_gold_to_have:
                    print("You no have money to continue game")
                    return True

                print("!!!!!")
                break
            print(111111)
            return False




    def item_types(self):
        print(colorama.Fore.YELLOW +'''
        ------------------
            Item type 
        ------------------
        ''')

        db = sqlite3.connect("Shop_DB.db")
        agent_tosya = db.cursor()

        agent_tosya.execute("SELECT name FROM item_types")
        data = agent_tosya.fetchall()

        self.display_menu(data,"item categories")
        answer = self.ask_answer(data)

        db.close()

        if answer == len(data)+1:
            self.welcome_board()
            return
        else:
            print(data[answer][0])
            eval(f"self.{data[answer][0]}()")
            self.item_types()



    def units(self):
        if len(self.team.team) > 4:
            print("Your team is full.Chose another shop")
            self.item_types()
            return
        print(colorama.Fore.LIGHTYELLOW_EX + f'''
                ------------------
                       UNITS 
                ------------------
                Gold = {self.gold}
                ''')
        db = sqlite3.connect("Shop_DB.db")
        agent_tosya = db.cursor()
        agent_tosya.execute("SELECT name, price FROM units")
        data = agent_tosya.fetchall()

        self.display_menu(data,"units")
        answer = self.ask_answer(data)

        if answer == len(data)+1:
            self.item_types()
            return

        name = data[answer][0]
        price = data[answer][1]

        print(name)
        print(price)


        if self.gold < price:
            print("You don't have money or this")
            #pragral tuta bomch
        match name:
            case "Knight":
                unit = UnitClases.Knight()
            case "Archer":
                unit = UnitClases.Archer()
            case "Healer":
                unit = UnitClases.Healer()
            case "Catapult":
                unit = UnitClases.Catapult()
            case "Defender":
                unit = UnitClases.Defender()
            case "Wizard":
                unit = UnitClases.Wizard()

        self.team.team.append(unit)
        self.gold -= price

        print(f'''
                You have bought {name} for {price} gold
        ''')
        db.close()

        if len(self.team.team) == 5:
            self.item_types()
        else:
            self.units()


    def armor(self):
        print(colorama.Fore.LIGHTRED_EX + f'''
                        ------------------
                               Armor 
                        ------------------
                        Gold = {self.gold}
                        ''')





        db = sqlite3.connect("Shop_DB.db")
        agent_tosya = db.cursor()

        unit = self.choose_unit()
        agent_tosya.execute(f"SELECT id, name FROM units WHERE name = '{unit.name}'")
        data = agent_tosya.fetchone()
        unit_id = data[0]

        agent_tosya.execute("SELECT name, usable_for_unit, value, price FROM armor")
        data = agent_tosya.fetchall()

        armor = self.choose_item(data,unit_id)
        armor_name = armor[0]
        armor_value = armor[2]
        armor_price = armor[3]

        db.close()

        if self.gold < armor_price:
            print("You don't have money for this")
            self.item_types()

        if eval(f"unit.{armor_name.split()[1]}.value") > armor_value:
            print(f"You already have better armor of {armor_name}")
            self.item_types()



        #perevircos chi nachas bronyas hirge za tu yaku mi hochemo kupitis
        #natyagnuti novi

        self.gold -= armor_price
        if armor_name.split()[1] == "helmet":
            unit.helmet.name = armor_name
            unit.helmet.value = armor_value
        elif armor_name.split()[1] == "bodyarmor":
            unit.bodyarmor.name = armor_name
            unit.bodyarmor.value = armor_value
        elif armor_name.split()[1] == "boots":
            unit.boots.name = armor_name
            unit.boots.value = armor_value
        elif armor_name.split()[1] == "shield":
            unit.shield.name = armor_name
            unit.shield.value = armor_value

        print(f"You succesfully have bought {armor_name} for {unit.name}.")
        print()

    def weapons(self):
        print(colorama.Fore.LIGHTWHITE_EX + f'''
                        ------------------
                               Armor 
                        ------------------
                        Gold = {self.gold}
                        ''')

        db = sqlite3.connect("Shop_DB.db")
        agent_tosya = db.cursor()

        unit = self.choose_unit()
        agent_tosya.execute(f"SELECT id, name FROM units WHERE name = '{unit.name}'")
        data = agent_tosya.fetchone()
        unit_id = data[0]

        agent_tosya.execute(f"SELECT name, usable_for_unit, value, price FROM weapons WHERE usable_for_unit = '{unit_id}'")
        data = agent_tosya.fetchall()

        weapon = self.choose_item(data,unit_id)
        weapon_name = weapon[0]
        weapon_value = weapon[2]
        weapon_price = weapon[3]

        db.close()

        if self.gold < weapon_price:
            print("You don't have money for this")
            self.item_types()
            return

        if eval(f"unit.{weapon_name.split()[1]}.value") > weapon_value:
            print(f"You already have better armor of {weapon_name}")
            self.item_types()
            return

        self.gold -= weapon_price
        unit.weapon.name = weapon_name
        unit.weapon.value = weapon_value

        print(f"You succesfully have bought {weapon_name} for {unit.name}.")
        print()

    def abilities(self):
        print(f'''
                        ------------------
                            Abilities
                        ------------------
                        Gold = {self.gold}
                        ''')

        db = sqlite3.connect("Shop_DB.db")
        agent_tosya = db.cursor()

        unit = self.choose_unit()
        agent_tosya.execute(f"SELECT id, name FROM units WHERE name = '{unit.name}'")
        data = agent_tosya.fetchone()
        unit_id = data[0]

        agent_tosya.execute(
            f"SELECT name, usable_for_unit, value, price FROM abilities WHERE usable_for_unit = '{unit_id}'")
        data = agent_tosya.fetchall()

        ability = self.choose_item(data,unit_id)
        ability_name = ability[0]
        ability_value = ability[2]
        ability_price = ability[3]

        db.close()

        if self.gold < ability_price:
            print("You don't have money for this")
            self.item_types()
            return

        if eval(f"unit.{ability_name.split()[1]}.value") > ability_value:
            print(f"You already have better armor of {ability_name}")
            self.item_types()
            return

        self.gold -= ability_price
        unit.ability.value = ability_value

        print(f"You succesfully have bought {ability_name} for {unit.name}.")
        print()