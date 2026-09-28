class Enemy(Entity):

    def aggro(self,target):     #not used
        if abs(self.pos[0] - target.pos[0]) <= 2 or abs(self.pos[1] - target.pos[1]) <= 2:
            self.attack(target)

    def drop_loot(self):
        return self.equip

    def name_with_prefix(self):
        lvl = self.lvl.current_lvl
        prefix = 'Timid' if lvl<10 else 'Trickster'
        if lvl >= 55: prefix = 'Legendary'
        elif lvl >= 45: prefix = 'Viscious'
        elif lvl >= 35: prefix = 'Snarling'       
        return f'{prefix} {self.name}'
