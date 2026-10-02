from character import Character
from inventory import Inventory
from quest import Quest
from weapon import Weapon
from armor import Armor

class Hero(Character):
    def __init__(   self,name,c_class=None,attrib=None,pos=None,equip=None,
                    lvl=1,gold=500,inv=None,quests=None,life=0):
        super().__init__(name,c_class,attrib,pos,equip,lvl)         #superclass Character init
        self.gold = gold                                            #player gold, not currently used
        self.inv = Inventory()                                      #player inventory
        self.quests = quests if quests else []                      #player quests
        self.life = life if life > 0 else self.max_life
    
    def char_type(self):
        return 'hero'

    def accept_quest(self,quest):
        self.quests.append(quest)

    def get_inventory(self):
        self.inv.list_items()

    def recieve_loot(self,xp,gold,*args):
        self.lvl.gain_xp(xp)
        self.gold += gold
        self.loot_item(*args)

    def loot_item(self, *args):
        for i in args: self.inv.add_item(i)