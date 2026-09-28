class Weapon(Item):
    def __init__(self,name,rarity,attrib,wep_type,dps):
        super().__init__(name,rarity,attrib)
        self.wep_type = wep_type
        self.dps = dps