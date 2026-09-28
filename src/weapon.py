import item as Item

wep_types = ['blunt','sharp','bow','magic']

class Weapon(Item):
    def __init__(self,name,rarity,attrib,wep_type='blunt',damage=10):
        super().__init__(name,rarity,attrib)
        self.wep_type = wep_type
        self.damage = damage
# 
    # def calculate_damage(base):
    #    return base + self.damage #* rarity_scalar[self.rarity])
# 
# iron_sword = Weapon('Iron Sword',wep_type='sharp',damage=10)
# wand = Weapon('Magic Wand',wep_type='magic',damage=12)
# short_bow = Weapon('Short bow',wep_type='bow',damage=8)
# fists = Weapon('Fists',wep_type='blunt',damage=5)