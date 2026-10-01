'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''
import os

from mainmenu import mainmenu
from combat import fight
from tools import loot_screen, show_inventory, screen_clear

from gameworld import GameWorld
from hero import Hero
from enemy import Enemy
from weapon import iron_sword,short_bow
from armor import plate_armors


gameworld = GameWorld('Pythonomia')
hero = Hero('Sir.Chadington','warrior',lvl=10)
enemy = Enemy('Goblin','warrior')
hero.equip_items(iron_sword)
# enemy.equip_items(short_bow)
# hero.equip_items(*plate_armors.values())

def main():
    mainmenu()
    gold,item = fight(hero,enemy)

    loot_screen(gold,item)
    show_inventory(hero)
    
if __name__ == '__main__':
    main()
