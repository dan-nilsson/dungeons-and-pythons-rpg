from character import Character

class Enemy(Character):
    def __init__(self,name,c_class=None,attrib=None,pos=None,equip=None,lvl=1):
        super().__init__(name,c_class,attrib,pos,equip,lvl)         #superclass Character init
        self.name = self.name_with_prefix()

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

    def drop_loot(self):
        return self.equip