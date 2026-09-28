import level
import hero,enemy
import weapon,armor

c_classes = ['warrior','wizard','beast']
init_attrib = { 'warrior' : {'stam' : 15, 'int' : 10, 'str' : 20, 'armor' : 0},
                'wizard' : {'stam': 15, 'int': 20, 'str': 10, 'armor' : 0}}
init_equip = {  'warrior' : {'wep' : Weapon('Fists'), 'armor' : 
                {'helm' : Armor('Leather Cap','helm',attrib={'stam' : 10, 'armor' : 15}), 'body' : None, 
                'gloves' : None, 'boots' : Armour('Leather Sandals','boots',attrib={'armor' : 15})}},
                'wizard' : {'wep' : Weapon('Fists'), 'armor' : 
                {'helm' : Armor('Linen Hat','helm',attrib={'int' : 10, 'armor' : 10}), 'body' : None, 
                'gloves' : None, 'boots' : Armour('Linen Slippers','boots',attrib={'armor' : 10})}},
                'beast' : None}


class Character:
    def __init__(self,name,c_class,attrib=None,pos=None,equip=None,lvl=None):
        self.name = name                                                        #character name
        self.c_class = c_class if c_class in c_classes else 'warrior'           #character class
        self.attrib = attrib if attrib else init_attrib[char_class].copy()      #character attributes
        self.pos = pos if pos else (0,0)                                        #not currently used
        self.equip = equip if equip else init_equip[c_class].copy()             #equipment
        self.lvl = lvl if lvl else Level(1)                                     #level, Level()
        self.calculate_init_health_mana()                                       #sets character life,mana from attrib
        self.is_alive = True                                                    #character is alive
        if isinstance(self,Enemy): self.name = self.name_with_prefix()

    def calculate_init_health_mana(self):
        self.max_life = self.attrib['stam'] * 10
        self.max_mana = self.attib['int'] * 10
        self.life, self.mana = self.max_life, self.max_mana

    def move(self,new_pos):
        self.pos = new_pos

    def attack(self,target):
        base_dmg = self.attrib['str'] * 10
        damage = self.equip['wep'].calculate_damage(base_dmg)
        crit = random.random() <= 0.2
        target.defend(damage * (2 if crit else 1))

    def defend(self,damage):
        dodge = random.random() <= 0.2
        if not dodge: self.take_dmg(damage)
        else: print(f'{self.name} dodges the attack.')      

    def take_dmg(self,dmg):
        final_dmg = dmg - self.attrib['armor']
        if final_dmg > 0: self.life -= final_dmg
        print(f'{self.name} takes {final_dmg} damage.')
        if not self.is_alive(): self.defeat()

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