#Base weapon class
class Weapon:
    #Durability, attack damage, range
    def __init__(self, damage_dice, damage_type, ability_score):
        self.damage_dice = damage_dice
        self.damage_type = damage_type
        self.ability_score = ability_score
    
    def attack(self):
        #roll a d20. Add proficiency bonus. Ability score. Compare to their armor class
        pass

class Simple_Melee:
    def __init__(self, type):
        pass

class Simple_Ranged:
    def __init__(self, type):
        pass

class Martial_Melee:
    def __init__(self, type):
        pass

class Martial_Ranged:
    def __init__(self, type):
        pass