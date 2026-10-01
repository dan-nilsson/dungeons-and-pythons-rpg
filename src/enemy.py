from random import randint

from character import Character

class Enemy(Character):
    def __init__(self,name,c_class=None,attrib=None,pos=None,equip=None,lvl=1):
        super().__init__(name,c_class,attrib,pos,equip,lvl)
        self.name = self.name_with_prefix()
        self.drop_gold = lvl*10*randint(1,5)

    def name_with_prefix(self):
        lvl = self.lvl.lvl
        prefix = 'Timid' if lvl<10 else 'Trickster'
        if lvl >= 55: prefix = 'Legendary'
        elif lvl >= 45: prefix = 'Viscious'
        elif lvl >= 35: prefix = 'Snarling'  
        return f'{prefix} {self.name}'

    def char_type(self):
        return 'enemy'

    def aggro(self,target):     #not used
        if abs(self.pos[0] - target.pos[0]) <= 2 or abs(self.pos[1] - target.pos[1]) <= 2:
            self.attack(target)

    def reset(self):
        self.is_alive = True
        self.heal(full=True)

    def calculate_drop_items(self) -> [Item]:
        return list(filter( lambda x: x is not None, 
                            [self.equip['wep']]+[a for a in self.equip['armor'].values()]))

    def give_reward(self):
        return self.lvl.lvl*100,self.drop_gold,self.calculate_drop_items()