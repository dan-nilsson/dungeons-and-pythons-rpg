from character import Character
from inventory import Inventory
from quest import Quest
from weapon import Weapon
from armor import Armor

class Hero(Character):
    def __init__(self,name,c_class,attrib=None,pos=None,equip=None,lvl=None,gold=500,inv=None,quests=None):
        super().__init__(name,c_class,attrib,pos,equip,lvl)      #superclass Character init
        self.gold = gold                                            #player gold, not currently used
        self.inv = inv if inv else Inventory()                      #player inventory
        self.quests = quests if quests else []                      #player quests
    
    def char_type(self):
        return 'hero'

    def accept_quest(self,quest):
        self.quests.append(quest)

    def get_inventory(self):
        self.inv.list_items()

    def loot_item(self, item) -> bool:
        return self.inv.add_item(item)

    def equip_item(self,*args):
        for item in args:
            if item.get_item_type() == 'wep':
                self.loot_item(self.equip['wep'])
                self.equip['wep'] = item
            else:
                self.loot_item(self.equip['armor'][item.get_slot()])
                self.equip['armor'][item.get_slot()] = item