import os

class HealthBar:

    filled,empty,end = '█','_','|'

    def __init__(self,char,len=30,is_colored=True,color='green'):
        self.char = char
        self.len = len
        self.max = self.char.max_life
        self.current = self.char.life

    def update(self) -> None:
        self.current = self.char.life

    def draw(self,damage=0,crit=False) -> None:
        num_filled = round((self.max / self.current) * self.len)
        num_lost = self.len - num_filled
        defend_action = f'-{damage}' if damage > 0 else 'DODGED' if damage == 0 else 'PARRIED'
        print(  self.char)
        print(  f'{self.end}{self.filled * num_filled}{self.empty * num_lost}{self.end}', 
                f'  {defend_action} {'CRITICAL!' if crit and damage > 0 else ''}')
