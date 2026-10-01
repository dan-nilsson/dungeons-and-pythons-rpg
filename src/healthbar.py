import os

class HealthBar:

    filled,empty,end = '█','_','|'

    def __init__(self,char,length=30,is_colored=True,color='green'):
        self.char = char
        self.length = length
        self.max = self.char.max_life
        self.current = self.char.life

    def update(self) -> None:
        self.max = self.char.max_life
        self.current = self.char.life

    def draw(self,damage=0,crit=False) -> [str]:
        num_filled = round((self.current / self.max) * self.length)
        num_lost = self.length - num_filled
        if (num_filled+num_lost) > self.length: num_lost -= 1
        defend_action = f'-{damage}' if damage >= 0 else 'DODGED' if damage == -1 else 'PARRIED'
        return  [f'{'{:<50}'.format(str(self.char))}',
                f'{self.end}{self.filled * num_filled}{self.empty * num_lost}{self.end}  '+
                f'{'{:<15}'.format(f'{defend_action} {'CRITICAL!' if crit and damage > 0 else ''}')}']
