import random

from level import Level
from inventory import Inventory
from quest import Quest
from weapon import fists
from armor import linen_armors,leather_armors
from healthbar import HealthBar

c_classes = [   'warrior','wizard','beast']
init_attrib = { 'warrior' : {'stam' : 15, 'int' : 10, 'str' : 20, 'armor' : 0},
                'wizard' : {'stam': 1-5, 'int': 20, 'str': 10, 'armor' : 0}}
init_equip = {  'warrior' : {'wep' : fists, 'armor' : 
                {'helm' : leather_armors['helm'], 'body' : None, 
                'gloves' : None, 'boots' : leather_armors['boots']}},
                'wizard' : {'wep' : fists, 'armor' : 
                {'helm' : linen_armors['helm'], 'body' : None, 
                'gloves' : None, 'boots' : linen_armors['boots']}},
                'beast' : None}

class Character:
    def __init__(self,name,c_class='warrior',attrib=None,pos=None,equip=None,lvl=1):
        self.name = name                                                        #character name
        self.c_class = c_class if c_class in c_classes else 'warrior'           #character class
        self.attrib = dict(init_attrib[self.c_class])                           #character attributes
        self.pos = pos if pos else (0,0)                                        #not currently used
        '''
        Had to hardcode equip for it not to be shared.
        '''
        self.equip = {'wep' : fists, 'armor' : 
                {'helm' : leather_armors['helm'], 'body' : None, 
                'gloves' : None, 'boots' : leather_armors['boots']}}            #equipment
        self.lvl = Level(lvl)                                                   #level, Level()
        self.apply_armor_effect()                                               #applies armor attributes to char
        self.calculate_health_mana()                                            #sets character life,mana from attrib
        self.is_alive = True                                                    #character is alive
        self.hp_bar = HealthBar(self)
        # print(init_equip['warrior']['armor']['helm'])

    def __str__(self) -> str:
        return f'{'{:<25}'.format(f'{self.lvl} {self.name}\'s')}' + f'HEALTH: {self.life}/{self.max_life}'

    def calculate_health_mana(self):
        self.max_life = self.attrib['stam'] * 10 + 500
        self.max_mana = self.attrib['int'] * 10 + 200
        self.life, self.mana = self.max_life, self.max_mana

    def apply_armor_effect(self):
        if not self.equip: return
        for armor in self.equip['armor'].values():
            if armor: armor.apply_attrib(self)
        self.calculate_health_mana()
    
    def equip_items(self,*args):
        for item in args:
            if item.get_item_type() == 'wep':
                if self.inv: self.loot_item(self.equip['wep'])
                self.equip['wep'] = item
            else:
                if self.equipped_armor(item.get_slot()) and self.inv:
                    self.loot_item(self.equip['armor'][item.get_slot()])
                self.equip['armor'][item.get_slot()] = item
        self.apply_armor_effect()

    def equipped_wep(self) -> Weapon:
        return self.equip['wep']

    def equipped_armor(self,slot=None) -> {Armor}:
        return self.equip['armor'] if not slot else self.equip['armor'][slot]

    def move(self,new_pos):
        self.pos = new_pos

    def attack(self,target):
        base_dmg = self.attrib['str'] * 2
        damage = self.equip['wep'].calculate_damage(base_dmg)
        crit = random.random() <= 0.2
        return target.defend(damage * (2 if crit else 1)), crit

    def defend(self,damage):
        dodge = random.random() <= 0.1
        parry = (random.random() if not self.equip['wep'] == fists else 1) <= 0.1
        if not dodge and not parry: 
            return self.take_dmg(damage)
        else:
            if parry: self.equipped_wep().lose_durability(1)
            # print(f'{self.name} {'dodges' if dodge else 'parries'} the attack.')
            return 0 if dodge else -1

    def take_dmg(self,dmg) -> float:
        final_dmg = dmg - self.attrib['armor']
        if final_dmg > 0: self.life -= final_dmg
        # print(f'{self.name} takes {final_dmg} damage.') # no longer needed with healthbar impl
        self.hp_bar.update()
        if self.life <= 0: self.is_alive = False
        return final_dmg

    def heal(self,amount):
        self.life += amount
        self.hp_bar.update()

    def defeat(self):
        suffix = 'has fallen' if self.char_type == 'hero' else 'is slain'
        print(f'{self.name} {suffix}.')