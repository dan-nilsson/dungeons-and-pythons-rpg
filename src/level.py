class Level:
    xp_per_level = 100

    def __init__(self,lvl,max_lvl=60,xp_multi=1.0):
        self.lvl = lvl
        self.max_lvl = max_lvl
        self.xp_multi = xp_multi
        self.current_xp = 0
    
    def __str__(self) -> str:
        return f'LVL.{self.lvl}'

    def gain_xp(self,xp):
        self.current_xp += xp
        self.gain_level_check()

    def gain_level_check(self):
        if self.current_xp >= self.xp_per_level:
            self.lvl += self.current_xp // self.xp_per_level
            if self.lvl > self.max_lvl: self.lvl = self.max_lvl
            self.current_xp = self.xp_per_level % self.current_xp

