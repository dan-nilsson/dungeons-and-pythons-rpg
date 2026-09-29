'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''

from gameworld import GameWorld
from hero import Hero
from enemy import Enemy
from weapon import iron_sword

gameworld = GameWorld('Pythonomia')
hero = Hero('Sir.Chadington','warrior')
hero.equip_item(iron_sword)
enemy = Enemy('Goblin')

def main():
    while True:
        hero_dmg,hero_crit = hero.attack(enemy)
        enemy_dmg,enemy_crit = enemy.attack(hero)

        hero.hp_bar.draw(hero_dmg,hero_crit)
        enemy.hp_bar.draw(enemy_dmg,enemy_crit)

        input()

if __name__ == '__main__':
    main()
