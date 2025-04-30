

class Armor():
    def __init__(self,init_name = None,init_value = 0):
        self.name = init_name
        self.value = init_value
class Weapon():
    def __init__(self,init_name = None,init_value = 0):
        self.name = init_name
        self.value = init_value

class Abilities():
    def __init__(self,init_name = None,init_value = 0,init_cooldown = None,init_description = ""):
        self.name = init_name
        self.value = init_value
        self.description = init_description
        self.cooldown = init_cooldown

        self.cooldown_left = self.cooldown