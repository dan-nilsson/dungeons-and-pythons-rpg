class Character:
    def __init__(self,name,pos,life,mana,equip,lvl):
        self.name = name
        self.pos = pos
        self.life = life
        self.mana = mana
        self.equip = equip
        self.lvl = lvl

    def move(self,new_pos):
        self.pos = new_pos

    def attack(self,entity):
        pass

    def defend(self,entity):
        pass

    def take_dmg(self,dmg):
        self.life -= dmg

    def heal(self,amount):
        self.life += amount