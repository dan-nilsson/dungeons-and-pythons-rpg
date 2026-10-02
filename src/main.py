'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''
from mainmenu import mainmenu
from gamemenu import gamemenu
from combat import fight
from tools import loot_screen, show_inventory, screen_clear

from gameworld import GameWorld
from hero import Hero
from enemy import Enemy
from weapon import iron_sword,short_bow

def main():
    active = False
    gameworld = None
    gamehero = None
    enemy = None
    
    while True:
        game,hero,reset = mainmenu(active,gameworld,gamehero)

        if not active or reset:
            gameworld = game
            gamehero = hero
            if not gameworld or not gamehero: continue
            gamehero.equip_items(iron_sword)
            gameworld.add_hero(gamehero)
            active = True

        gamemenu(gameworld,gamehero)
    
if __name__ == '__main__':
    main()
