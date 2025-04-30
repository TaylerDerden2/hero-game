from .Unit import Unit
from .Items import Abilities

class Knight(Unit):

    def __init__(self,init_name = "Knight",init_health_default = 700,init_attack_default = 200):
        self.name = init_name
        self.health_default = init_health_default
        self.attack_default = init_attack_default

        self.ability = Abilities("SplashAttack", 0.5, 4, "He splash all enemy unites at 50% of his power")