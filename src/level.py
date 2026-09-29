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