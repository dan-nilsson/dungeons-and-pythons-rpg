'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''

class Entity:
    def __init__(self,name,pos,life,equip):
        self.name = name
        self.pos = pos
        self.life = life
        self.equip = equip

    def move(self,new_pos):
        self.pos = new_pos

    def attack(self,entity):
        pass

    def take_dmg(self,dmg):
        self.life -= dmg

    def heal(self,amount):
        self.life += amount

class Character(Entity):
    def __init__(self,name,pos,life,equip,c_class,inv,quests):
        super().__init__(name,pos,life,equip)
        self.c_class = c_class
        self.inv = inv
        self.quests = quests

    def accept_quest(self,quest):
        pass

    def get_inventory(self):
        pass

    def equip_item(self):
        pass

class Enemy(Entity):
    def aggro(self):
        pass

class Item:
    def __init__(self,name,rarity,attrib):
        self.name = name
        self.rarity = rarity
        self.attrib = attrib

class Weapon(Item):
    def __init__(self,name,rarity,attrib,wep_type,dps):
        super().__init__(name,rarity,attrib)
        self.wep_type = wep_type
        self.dps = dps

class Armor(Item):
    def __init__(self,name,rarity,attrib,slot,armor):
        super().__init__(name,rarity,attrib)
        self.slot = slot
        self.armor = armor

class Inventory:
    def __init__(self,size,layout):
        self.size = size
        self.layout = layout

class Quest:
    def __init__(self,name,giver,objective,reward):
        self.name = name
        self.giver = giver
        self.objective = objective
        self.reward = reward

    def complete_quest(self,char):
        pass

    def give_reward(self,char):
        pass

class Level:
    xp_per_level = 100

    def __init__(self,current_lvl,max_lvl,xp_multi):
        self.current_lvl = current_lvl
        self.max_lvl = max_lvl
        self.xp_multi

    def gain_xp(self):
        pass

class Location:
    biome_to_enemy = {'cave' : ['bear'], 'desert' : ['scorpion']}

    def __init__(self,name,biome):
        self.name = name
        self.biome = biome

class Stats:
    pass



def main():
    pass

if __name__ == '__main__':
    main()
