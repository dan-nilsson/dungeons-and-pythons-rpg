import level

init_attrib = { 'warrior' : {'stam' : 15, 'int' : 10, 'str' : 20},
                'wizard' : {'stam': 15, 'int': 20, 'str': 10}
}

class Character:
    def __init__(self,name,char_class,attrib=None,pos=None,equip=None,lvl=None):
        self.name = name                                                        #character name
        self.char_class = char_class                                            #character class
        self.attrib = attrib if attrib else init_attrib[char_class].copy()      #character attributes
        self.pos = pos if pos else (0,0)                                        #not currently used
        self.equip = equip if equip else []                                     #equipment
        self.lvl = lvl if lvl else Level(1)                                     #level, Level()
        self.calculate_init_health_mana()                                       #sets character life,mana from attrib
        self.is_alive = True                                                    #character is alive

    def calculate_init_health_mana(self):
        self.max_life = self.attrib['stam'] * 10
        self.max_mana = self.attib['int'] * 10
        self.life, self.mana = self.max_life, self.max_mana

    def move(self,new_pos):
        self.pos = new_pos

    def attack(self,target):
        damage = self.attrib['str'] * 10
        crit = random.random() <= 0.2
        target.defend(damage * (2 if crit else 1))

    def defend(self,damage):
        dodge = random.random() <= 0.2
        if not dodge: self.take_dmg(damage)
        else: print(f'{self.name} dodges the attack.')      

    def take_dmg(self,dmg):
        self.life -= dmg
        print(f'{self.name} takes {dmg} damage.')
        if not self.is_alive(): self.defeat()

    def heal(self,amount):
        self.life += amount

    def calculate_equip_effect(self):
        for e in self.equip:
            pass

    def is_alive(self):
        if self.life <= 0: self.is_alive = False
        return self.is_alive

    def defeat(self):
        print(f'Character {self.name} is defeated.')