class Location:
    biomes = set(['village','castle','forest','cave','desert','boss_lair'])
    biome_to_enemy = {  'forest': ['Wolf','Bandit'],
                        'field' : ['Cougar','Ruffian'],
                        'cave' : ['Bear','Ghost'],
                        'desert' : ['Scorpion','Snake'],
                        'boss_lair' : ['Dragon']}

    def __init__(self,name,biome=None,is_hostile=False):
        self.name = name
        self.biome = biome if biome in biomes else 'village'
        self.is_hostile = is_hostile

    def enemy_types(self):
        return biome_to_enemy[self.biome] if self.is_hostile else None