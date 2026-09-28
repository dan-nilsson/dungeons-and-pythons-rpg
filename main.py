'''
Python Fundamentals Project - Fantasy Adventure / RPG Game
Dungeons & Pythons
'''

import src.gameworld as GameWorld
import src.hero as Hero
import src.enemy as Enemy

gameworld = GameWorld('Pythonomia')
hero = Hero('Sir.Chadington','warrior')
enemy = Enemy('Goblin')

while True:
    hero_dmg,hero_crit = hero.attack(enemy)
    enemy_dmg,enemy_crit = enemy.attack(hero)

    print('attackkeee')

def main():
    pass

if __name__ == '__main__':
    main()
