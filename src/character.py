import random

from level import Level
from inventory import Inventory
from quest import Quest
from weapon import fists
from armor import linen_armors,leather_armors
from healthbar import HealthBar

c_classes = ['warrior','wizard','beast']
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
    def __init__(self,name,c_class='warrior',attrib=None,pos=None,equip=None,lvl=None):
        self.name = name                                                        #character name
        self.c_class = c_class                                                  #character class
        self.attrib = attrib if attrib else init_attrib[c_class].copy()         #character attributes
        self.pos = pos if pos else (0,0)                                        #not currently used
        self.equip = equip if equip else init_equip[c_class].copy()             #equipment
        self.lvl = lvl if lvl else Level(1)                                     #level, Level()
        self.calculate_armor_effect()                                           #applies armor attributes to char
        self.calculate_init_health_mana()                                       #sets character life,mana from attrib
        self.is_alive = True                                                    #character is alive
        self.hp_bar = HealthBar(self)

    def __str__(self):
        return f'{self.name}\'s HEALTH: {self.life}/{self.max_life}'

    def calculate_init_health_mana(self):
        self.max_life = self.attrib['stam'] * 10 + 500
        self.max_mana = self.attrib['int'] * 10 + 200
        self.life, self.mana = self.max_life, self.max_mana

    def calculate_armor_effect(self):
        if not self.equip: return
        for armor in self.equip['armor'].values():
            if armor: armor.apply_attrib(self) 

    def equipped_wep(self) -> Weapon:
        return self.equip['wep']

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
        if not self.is_alive: self.defeat()
        return final_dmg

    def heal(self,amount):
        self.life += amount
        self.hp_bar.update()

    def defeat(self):
        suffix = 'defeated' if self.char_type == 'hero' else 'slain'
        print(f'{self.name} is {suffix}.')