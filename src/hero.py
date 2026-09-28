import inventory

class Hero(Character):
    def __init__(self,name,char_class,attrib=None,pos=None,equip=None,lvl=None,gold=500,inv=None,quests=None):
        super().__init__(name,char_class,attrib,pos,equip,lvl)      #superclass Character init
        self.gold = gold                                            #player gold, not currently used
        self.inv = inv if inv else Inventory()                      #player inventory
        self.quests = quests if quests else []                      #player quests

    def accept_quest(self,quest):
        self.quests.append(quest)

    def get_inventory(self):
        self.inv.list_items()

    def loot_item(self, item) -> bool:
        return self.inv.add_item(item)

    def equip_item(self,item):
        super().equip.append(item)
        self.inv.remove_item(item)