import hero,enemy
import location

class GameWorld:
    world_layout =  [   [None,None,None],
                        [None,None,None],
                        [None,None,None]]

    def __init__(self,name,locations=None,current_pos=(0,0)):
        self.name = name 
        self.locations = locations if locations else world_layout.copy()
        self.current_pos = current_pos

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
            


