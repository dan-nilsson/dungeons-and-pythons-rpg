class Location:
    biomes = set(['village','castle','forest','cave','desert'])
    biome_to_enemy = {'forest': ['wolf'],'cave' : ['bear'],'desert' : ['scorpion']}

    def __init__(self,name,biome=None,is_hostile=False):
        self.name = name
        self.biome = biome if biome in biomes else 'village'
        self.is_hostile = is_hostile

    def enemy_types(self):
        return biome_to_enemy[self.biome] if self.is_hostile else None