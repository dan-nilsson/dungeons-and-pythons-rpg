'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''
import os

from gameworld import GameWorld
from hero import Hero
from enemy import Enemy
from weapon import iron_sword,short_bow
from armor import plate_armors

gameworld = GameWorld('Pythonomia')
hero = Hero('Sir.Chadington','warrior',lvl=10)
enemy = Enemy('Goblin')
hero.equip_items(iron_sword)
# hero.equip_items(*plate_armors.values())
enemy.equip_items(short_bow)

def main():
    fight()
        
def fight() -> None:
    while True:
        screen_clear()

        e_dmg,e_crit = hero.attack(enemy)
        h_dmg,h_crit = enemy.attack(hero)

        print('/'*15,'  FIGHT  ','/'*15)
        hero.hp_bar.draw(h_dmg,h_crit)
        enemy.hp_bar.draw(e_dmg,e_crit)

        if hero.is_alive and enemy.is_alive:
            input()
        else: 
            enemy.defeat() if hero.is_alive else hero.defeat()
            # hero.equipped_wep().check_durability()
            # print(gameworld)
            # print(hero.lvl)
            # print(hero.attrib)
            # print(hero.life)
            # print(hero.max_life)
            # print(hero.equipped_armor())
            # enemy.equipped_wep().check_durability()
            break

def screen_clear() -> None:
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

if __name__ == '__main__':
    main()
