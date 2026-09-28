'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''

from gameworld import GameWorld
from character import Hero,Enemy
from item import iron_sword

gameworld = GameWorld('Pythonomia')
hero = Hero('Sir.Chadington','warrior')
hero.equip_item(iron_sword)
enemy = Enemy('Goblin')

def main():
    while True:
        hero_dmg,hero_crit = hero.attack(enemy)
        enemy_dmg,enemy_crit = enemy.attack(hero)
        print(hero_dmg,hero_crit)
        print(hero.equip['armor']['helm'].name)
        input()

if __name__ == '__main__':
    main()
