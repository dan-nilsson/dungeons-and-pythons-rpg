class Item:
    item_rarities = set(['Common','Rare','Epic','Legendary'])
    rarity_scalar = {'Common' : 1, 'Rare' : 1.5, 'Epic' : 2, 'Legendary' : 5}

    def __init__(self,name,rarity='Common',attrib=None):
        self.name = name
        self.rarity = rarity
        self.attrib = attrib
        self.durability = 100
        self.broken = False

    def apply_attrib(self,char):
        if not self.attrib: return
        for k,v in self.attrib.items():
            char.attrib[k] += v * rarity_scalar[self.rarity]

    def lose_durability(self,amount):
        self.durability -= amount
        if self.durability <= 0: self.broken = True

    def repair_durability(self):
        self.durability = 100

    def check_durability(self):
        print(f'Current durability for {self.name} is {self.durability}.')
        return self.durability
