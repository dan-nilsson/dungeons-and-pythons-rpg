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
hero = Hero('Sir.Chadington','warrior',lvl=50)
enemy = Enemy('Goblin')
# print(hero.attrib)
print(enemy.equipped_armor())
hero.equip_items(iron_sword)
hero.equip_items(*plate_armors.values())
print(enemy.equipped_armor())

# print(hero.attrib)
# print(hero.equipped_armor())
# print(enemy.equipped_armor())
# print(enemy.attrib)
# print(enemy.equipped_wep())

def main():
    fight()
        
def fight() -> None:
    while True:
        # screen_clear()

        e_dmg,e_crit = hero.attack(enemy)
        h_dmg,h_crit = enemy.attack(hero)

        print('/'*15,'  FIGHT  ','/'*15)
        hero.hp_bar.draw(h_dmg,h_crit)
        enemy.hp_bar.draw(e_dmg,e_crit)

        if hero.is_alive and enemy.is_alive:
            input()
        else: 
            enemy.defeat() if hero.is_alive else hero.defeat()
            hero.equipped_wep().check_durability()
            # print(gameworld)
            # print(hero.lvl)
            break

def screen_clear() -> None:
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

if __name__ == '__main__':
    main()
