'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''

'''
Imports wont work in /src folder.
Working on main.py in /src until I can solve import issues
'''
# 
# from src.gameworld import GameWorld
# from src.hero import Hero
# from src.character import Enemy
# 
import src.loop as loop
# gameworld = GameWorld('Pythonomia')
# hero = Hero('Sir.Chadington','warrior')
# enemy = Enemy('Goblin')

def main():
    loop.run()

if __name__ == '__main__':
    main()
