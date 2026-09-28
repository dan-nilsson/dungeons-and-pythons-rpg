wep_types = ['blunt','sword','bow','magic']

class Weapon(Item):
    def __init__(self,name,rarity='Common',attrib=None,wep_type='blunt'):
        super().__init__(name,rarity,attrib)
        self.wep_type = wep_type

    def calculate_damage(self,base):
        return base * rarity_scalar[self.rarity]