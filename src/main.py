'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''

from gameworld import GameWorld
from hero import Hero
from character import Enemy

gameworld = GameWorld('Pythonomia')
hero = Hero('Sir.Chadington','warrior')
enemy = Enemy('Goblin')

def main():
    while True:
        hero_dmg,hero_crit = hero.attack(enemy)
        enemy_dmg,enemy_crit = enemy.attack(hero)
        print('attackkeee')
        input()

if __name__ == '__main__':
    main()
