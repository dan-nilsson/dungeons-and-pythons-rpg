class Location:
    biome_to_enemy = {'cave' : ['bear'], 'desert' : ['scorpion']}

    def __init__(self,name,biome,grid):
        self.name = name
        self.biome = biome
        self.grid = grid