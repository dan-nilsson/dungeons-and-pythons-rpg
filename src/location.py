class Location:
    biomes = set(['village','castle','forest','cave','desert','boss_lair'])
    biome_to_enemy = {  'forest': ['Wolf','Bandit'],
                        'field' : ['Cougar','Ruffian'],
                        'cave' : ['Bear','Ghost'],
                        'village' : ['Donkey','Thief'],
                        'desert' : ['Scorpion','Snake'],
                        'boss_lair' : ['Dragon']}

    def __init__(self,name='Pythonburg',biome=None,is_hostile=False):
        self.name = name
        self.biome = biome if biome in self.biomes else 'village'
        self.is_hostile = is_hostile

    def __str__(self) -> str:
        return self.name_with_prefix()

    def name_with_prefix(self):
        match self.biome:
            case 'village' | 'castle':
                prefix = 'shady' if self.is_hostile else 'quaint'
            case 'forest' | 'cave':
                prefix = 'spooky' if self.is_hostile else 'tranquile'
            case 'desert':
                prefix = 'scorching' if self.is_hostile else 'dry'
            case 'boss_lair':
                prefix = 'darkness'
        return f'{prefix.capitalize()} {self.name}'

    def enemy_types(self):
        return self.biome_to_enemy[self.biome] if self.is_hostile else None

locations =[[Location('Pythonburg','village'),Location('Greensholme','forest',True),Location('Sandsweep','desert',True)],
            [Location('Bear Home','cave',True),Location('Treewoods','forest',True),Location('Aridania','desert',True)],
            [Location('Pythonston','village',True),Location('Elwynn','forest',True),Location('Silithus','desert',True)]]