from .Unit import Unit
from .Items import Abilities

class Catapult(Unit):

    def __init__(self,init_name = "Catapult",init_health_default= 700,init_attack_default= 150):
        self.name = init_name
        self.health_default = init_health_default
        self.attack_default = init_attack_default

        self.ability = Abilities("SuperAttack", 2,4,"Catapult hits 2x damage to choose enemy unit")