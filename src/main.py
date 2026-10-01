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

def main():
    active = False
    gameworld = None
    hero = None
    enemy = Enemy('Goblin','warrior')
    enemy.equip_items(short_bow)
    # hero.equip_items(*plate_armors.values())
    
    while True:
        game,hero = mainmenu(active)
        w_name,h_name,h_class = game[0],hero[0],hero[1]

        gameworld = GameWorld(w_name)
        hero = Hero(h_name,h_class)
        hero.equip_items(iron_sword)
        active = True
        xp,gold,item = fight(hero,enemy)

        loot_screen(xp,gold,item)
        show_inventory(hero)
    
if __name__ == '__main__':
    main()
