'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''
import os

from mainmenu import mainmenu
from gamemenu import gamemenu
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
    gamehero = None
    enemy = Enemy('Goblin','warrior')
    enemy.equip_items(short_bow)
    # hero.equip_items(*plate_armors.values())
    
    while True:
        game,hero,reset = mainmenu(active,gameworld,gamehero)

        if not active or reset:
            gameworld = game if game else GameWorld('Pythomania')
            gamehero = hero if hero else Hero('Default')
            gamehero.equip_items(iron_sword)
            enemy.reset()
            active = True

        gamemenu(gameworld,gamehero)

        xp,gold,item = fight(hero,enemy)

        loot_screen(xp,gold,item)
        show_inventory(hero)
    
if __name__ == '__main__':
    main()
