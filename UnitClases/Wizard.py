from .Unit import Unit
from .Items import Abilities

class Wizard(Unit):

    def __init__(self,init_name = "Wizard",init_health_default= 700,init_attack_default= 150):
        self.name = init_name
        self.health_default = init_health_default
        self.attack_default = init_attack_default

        self.ability = Abilities("SuperStun", 1, 4, "He can stun all enemy units for the next fight")