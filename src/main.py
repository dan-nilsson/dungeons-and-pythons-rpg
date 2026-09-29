'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''
import os

from gameworld import GameWorld
from hero import Hero
from enemy import Enemy
from weapon import iron_sword
from armor import plate_armors

gameworld = GameWorld('Pythonomia')
hero = Hero('Sir.Chadington','warrior')
hero.equip_item(iron_sword)
hero.equip_item(plate_armors['helm'])
enemy = Enemy('Goblin')

def main():
    while True:
        screen_clear()

        hero_dmg,hero_crit = hero.attack(enemy)
        enemy_dmg,enemy_crit = enemy.attack(hero)

        hero.hp_bar.draw(hero_dmg,hero_crit)
        enemy.hp_bar.draw(enemy_dmg,enemy_crit)

        print(hero.inv)

        input()

def screen_clear() -> None:
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

if __name__ == '__main__':
    main()
