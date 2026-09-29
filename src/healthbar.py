import os

class HealthBar:

    filled,empty,end = '█','_','|'

    def __init__(self,char,len=20,is_colored=True,color='green'):
        self.char = char
        self.len = len
        self.max = self.char.max_life
        self.current = self.char.life

    def update(self) -> None:
        self.current = self.char.life

    def draw(self,damage=0,crit=False) -> None:
        num_filled = round(self.current / self.max * self.len)
        num_lost = self.len - num_filled
        print(  f'{self.char.name}\'s HEALTH: {self.char.life}/{self.char.max_life}')
        print(  f'{self.end}{self.filled * num_filled}{self.empty * num_lost}{self.end}', 
                f'  {f'-{damage}' if damage else 'DODGED'} {'CRITICAL!' if crit and damage else ''}')
