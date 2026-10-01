from tools import screen_clear

def fight(hero,enemy):
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
            '''
            Lotsa testing. Don't mind me.
            '''
            # hero.equipped_wep().check_durability()
            # print(gameworld)
            # print(hero.lvl)
            # print(hero.attrib)
            # print(enemy.attrib)
            # print(hero.life)
            # print(hero.max_life)
            # print(hero.equipped_armor())
            # print(enemy.equipped_armor())
            # enemy.equipped_wep().check_durability()
            if hero.is_alive:
                xp,gold,items = enemy.give_reward()
                enemy.defeat()
                hero.recieve_loot(xp,gold,*items)
                return xp,gold,items
            else: 
                hero.defeat()
                return None,None,None