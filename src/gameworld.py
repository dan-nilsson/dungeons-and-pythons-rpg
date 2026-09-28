from hero import Hero
from character import Enemy
from location import Location

class GameWorld:
    world_layout =  [   [None,None,None],
                        [None,None,None],
                        [None,None,None]]

    def __init__(self,name,locations=None,current_pos=(0,0)):
        self.name = name 
        self.locations = locations if locations else self.world_layout.copy()
        self.current_pos = current_pos
        # self.hero = None
        # self.enemy = None
# 
    # def add_hero(self,hero):
        # if not self.hero: self.hero = hero
# 
    # def add_enemy(self,enemy):
        # if not self.enemy: self.enemy = enemy

    def add_locations(self,*args):
        for loc in args:
            for row in range(len(self.locations)):
                for col in range(len(self.locations[row])):
                    if not locations[row][col]: self.locations[row][col] = loc
                    if row == 2 and col == 2 and self.locations[row][col]:
                        print(f'No room for location in GameWorld')
                        break
    
    def current_location(self):
        x,y = self.current_pos[0],current_pos[1]
        return self.locations[y][x]
            


