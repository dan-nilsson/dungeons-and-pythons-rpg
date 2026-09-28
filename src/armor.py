armor_slots = ['helm','body','gloves','boots']

class Armor(Item):
    def __init__(self,name,slot,rarity='Common',attrib=None):
        super().__init__(name,rarity,attrib)
        self.slot = slot if slot in armor_slots else 'unknown'

    def get_slot(self):
        return self.slot

    