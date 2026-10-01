from tools import screen_clear, draw_sep, draw_line, draw_lines_centered

fight_header = f'{'/'*15}  FIGHT  {'/'*15}'
width = 60

def fight(hero,enemy):
    while True:
        screen_clear()

        e_dmg,e_crit = hero.attack(enemy)
        h_dmg,h_crit = enemy.attack(hero)

        h_bar = hero.hp_bar.draw(h_dmg,h_crit)
        e_bar = enemy.hp_bar.draw(e_dmg,e_crit)
        draw_lines_centered([fight_header]+h_bar+e_bar,width,pad_over=1,pad_under=1)

        if hero.is_alive and enemy.is_alive:
            input()
        else: 
            if hero.is_alive:
                xp,gold,items = enemy.give_reward()
                enemy.defeat()
                hero.recieve_loot(xp,gold,*items)
                return xp,gold,items
            else: 
                hero.defeat()
                return None,None,None