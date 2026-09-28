class Armor(Item):
    def __init__(self,name,rarity,attrib,slot,armor):
        super().__init__(name,rarity,attrib)
        self.slot = slot
        self.armor = armor