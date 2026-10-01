from hero import Hero
from enemy import Enemy
from location import Location,locations

class GameWorld:
    def __init__(self,name,locations=None,current_pos=(0,0)):
        self.name = name 
        self.locations = [  [None,None,None],
                            [None,None,None],
                            [None,None,None]]
        self.current_pos = current_pos
        self.hero = None
        self.enemies = []
        self.add_locations(locations)

    def __str__(self):
        return '\n'.join([str(row) for row in self.locations])

    def add_hero(self,hero):
        if not self.hero: self.hero = hero

    def add_enemy(self,enemy):
        self.enemies.append(enemy)

    def add_locations(self,*args):      #will impl loop later
        self.locations = locations
        # for loc in args:
            # for row in range(len(self.locations)):
                # for col in range(len(self.locations[row])):
                    # if not locations[row][col]: self.locations[row][col] = loc
                    # if row == 2 and col == 2 and self.locations[row][col]:
                        # break
    
    def update_pos(self,pos):
        self.current_pos = pos
        
    def current_location(self):
        x,y = self.current_pos
        return self.locations[y][x]