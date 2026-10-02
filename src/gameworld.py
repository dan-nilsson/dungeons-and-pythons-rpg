import random, copy

from hero import Hero
from enemy import Enemy
from location import Location,locations
from weapon import short_bow

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

    def add_enemy(self):
        enemy = Enemy(random.choice(self.current_location().enemy_types()))
        enemy.equip_items(short_bow)
        self.enemies.append(enemy)

    def pick_enemy(self) -> Enemy:
        enemy = self.enemies.pop()
        if not self.enemies: self.current_location().is_hostile = False
        return enemy

    def reset_map(self):
        self.add_locations()

    def add_locations(self,*args):      #will impl loop later
        self.locations = copy.deepcopy(locations)
        # for loc in args:
        #     for row in range(len(self.locations)):
        #         for col in range(len(self.locations[row])):
        #             if not locations[row][col]: self.locations[row][col] = loc
        #             if row == 2 and col == 2 and self.locations[row][col]:
        #                 break
    
    def current_location(self):
        x,y = self.current_pos
        return self.locations[y][x]
    
    def update_pos(self,pos):
        self.current_pos = pos
        self.hero.pos = self.current_pos

    def move(self,direction):
        x,y = self.current_pos
        if self.movement_allowed(direction):
            match direction:
                case 'N': self.update_pos((x,y-1))
                case 'S': self.update_pos((x,y+1))
                case 'W': self.update_pos((x-1,y))
                case 'E': self.update_pos((x+1,y))

    def movement_allowed(self,direction):
        x,y = self.current_pos
        match direction:
            case 'N': return y != 0
            case 'S': return y != 2
            case 'W': return x != 0
            case 'E': return x != 2