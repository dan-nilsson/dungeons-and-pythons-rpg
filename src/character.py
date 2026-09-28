import random

from level import Level
from weapon import fists
from armor import linen_armors,leather_armors

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
        self.attrib = attrib if attrib else init_attrib[c_class].copy()      #character attributes
        self.pos = pos if pos else (0,0)                                        #not currently used
        self.equip = equip if equip else init_equip[c_class].copy()             #equipment
        self.lvl = lvl if lvl else Level(1)                                     #level, Level()
        self.calculate_init_health_mana()                                       #sets character life,mana from attrib
        self.is_alive = True                                                    #character is alive
        if isinstance(self,Enemy): self.name = self.name_with_prefix()

    def calculate_init_health_mana(self):
        self.max_life = self.attrib['stam'] * 10
        self.max_mana = self.attrib['int'] * 10
        self.life, self.mana = self.max_life, self.max_mana

    def move(self,new_pos):
        self.pos = new_pos

    def attack(self,target):
        base_dmg = self.attrib['str'] * 10
        damage = self.equip['wep'].calculate_damage(base_dmg)
        crit = random.random() <= 0.2
        return target.defend(damage * (2 if crit else 1)), crit

    def defend(self,damage):
        dodge = random.random() <= 0.2
        if not dodge: self.take_dmg(damage)
        else: print(f'{self.name} dodges the attack.')      

    def take_dmg(self,dmg):
        final_dmg = dmg - self.attrib['armor']
        if final_dmg > 0: self.life -= final_dmg
        print(f'{self.name} takes {final_dmg} damage.')
        if not self.is_alive: self.defeat()

    def heal(self,amount):
        self.life += amount

    def calculate_armor_effect(self):
        if not self.equip: return
        for armor in self.equip['armor'].values():
            armor.apply_attrib(self)

    def is_alive(self):
        if self.life <= 0: self.is_alive = False
        return self.is_alive

    def defeat(self):
        print(f'Character {self.name} is defeated.')

class Enemy(Character):
    def __init__(self,name,c_class='warrior',attrib=None,pos=None,equip=None,lvl=None):
        super().__init__(name,c_class,attrib,pos,equip,lvl)         #superclass Character init

    def aggro(self,target):     #not used
        if abs(self.pos[0] - target.pos[0]) <= 2 or abs(self.pos[1] - target.pos[1]) <= 2:
            self.attack(target)

    def drop_loot(self):
        return self.equip
        
    def name_with_prefix(self):
        lvl = self.lvl.current_lvl
        prefix = 'Timid' if lvl<10 else 'Trickster'
        if lvl >= 55: prefix = 'Legendary'
        elif lvl >= 45: prefix = 'Viscious'
        elif lvl >= 35: prefix = 'Snarling'  
        return self.name     
        return f'{prefix} {self.name}'