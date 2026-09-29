from item import Item

wep_types = ['blunt','sharp','bow','magic']

class Weapon(Item):
    def __init__(self,name,rarity='Common',attrib=None,wep_type='blunt',damage=10):
        super().__init__(name,rarity,attrib)
        self.wep_type = wep_type
        self.damage = damage

    def get_item_type(self):
        return 'wep'
        
    def calculate_damage(self,base):
       return base + (self.damage * self.rarity_scalar[self.rarity])

iron_sword = Weapon('Iron Sword',wep_type='sharp',damage=50)
wand = Weapon('Magic Wand',wep_type='magic',damage=100)
short_bow = Weapon('Short bow',wep_type='bow',damage=30)
fists = Weapon('Fists',wep_type='blunt',damage=1)