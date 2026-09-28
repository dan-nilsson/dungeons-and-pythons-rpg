class Item:
    item_rarities = set(['Common','Rare','Epic','Legendary'])
    rarity_scalar = {'Common' : 1, 'Rare' : 1.5, 'Epic' : 2, 'Legendary' : 5}

    def __init__(self,name,rarity='Common',attrib=None):
        self.name = name
        self.rarity = rarity
        self.attrib = attrib
        self.durability = 100
        self.broken = False

    def get_type(self):
        return 'wep' if isinstance(self,Weapon) else 'armor'

    def apply_attrib(self,char):
        if not self.attrib: return
        for k,v in self.attrib.items():
            char.attrib[k] += v * self.rarity_scalar[self.rarity]

    def lose_durability(self,amount):
        self.durability -= amount
        if self.durability <= 0: self.broken = True

    def repair_durability(self):
        self.durability = 100

    def check_durability(self):
        print(f'Current durability for {self.name} is {self.durability}.')
        return self.durability

wep_types = ['blunt','sharp','bow','magic']

class Weapon(Item):
    def __init__(self,name,rarity='Common',attrib=None,wep_type='blunt',damage=10):
        super().__init__(name,rarity,attrib)
        self.wep_type = wep_type
        self.damage = damage
# 
    def calculate_damage(self,base):
       return base + (self.damage * self.rarity_scalar[self.rarity])

iron_sword = Weapon('Iron Sword',wep_type='sharp',damage=10)
wand = Weapon('Magic Wand',wep_type='magic',damage=12)
short_bow = Weapon('Short bow',wep_type='bow',damage=8)
fists = Weapon('Fists',wep_type='blunt',damage=1)

armor_slots = ['helm','body','gloves','boots']

class Armor(Item):
    def __init__(self,name,slot,rarity='Common',attrib=None):
        super().__init__(name,rarity,attrib)
        self.slot = slot if slot in armor_slots else 'unknown'

    def get_slot(self):
        return self.slot

linen_armors = {    'helm' : Armor('Linen Hat','helm',attrib={'int':10,'armor':10}),
                    'body' : Armor('Linen Robe','body',attrib={'int':15,'armor' : 10}),
                    'gloves' : Armor('Linen Mits','gloves',attrib={'armor' : 10}),
                    'boots' : Armor('Linen Slippers','boots',attrib={'armor' : 10})
}
leather_armors = {  'helm' : Armor('Leather Cap','helm',attrib={'stam':10,'armor':15}),
                    'body' : Armor('Leather Tunic','body',attrib={'stam':15,'armor' : 15}),
                    'gloves' : Armor('Leather Handwraps','gloves',attrib={'str':10,'armor' : 15}),
                    'boots' : Armor('Leather Boots','boots',attrib={'armor' : 15})
}
plate_armors = {    'helm' : Armor('Plate Visor','helm',attrib={'stam':10,'armor':20}),
                    'body' : Armor('Plate Breastplate','body',attrib={'stam':15,'armor' : 20}),
                    'gloves' : Armor('Plate Handguards','gloves',attrib={'stam':10,'armor' : 20}),
                    'boots' : Armor('Plate Stirrups','boots',attrib={'armor' : 20})
}