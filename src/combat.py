from tools import screen_clear, draw_sep, draw_line_left, draw_lines_aligned

fight_header = f'{'/'*15}  FIGHT  {'/'*15}'
width = 60

def fight(hero,enemy):
    choice = '1'
    while True:
        screen_clear()

        match choice.lower():
            case '2' | 'heal':
                hero.heal()
                e_dmg,e_crit = 0,False
                h_dmg,h_crit = enemy.attack(hero)
            case _:
                e_dmg,e_crit = hero.attack(enemy)
                h_dmg,h_crit = enemy.attack(hero)

        h_bar = hero.hp_bar.draw(h_dmg,h_crit)
        e_bar = enemy.hp_bar.draw(e_dmg,e_crit)

        draw_lines_aligned([fight_header]+h_bar+e_bar,width,pad_over=1,pad_under=1)
        print(draw_line_left('   1. ATTACK 2. heal',width=width))
        draw_sep(width)

        if hero.is_alive and enemy.is_alive:
            choice = input('>>>  ')
        else: 
            if hero.is_alive:
                draw_lines_aligned(enemy.defeat(hero.name),width=width,pad_over=2,pad_under=3,pause=3)

                xp,gold,items = enemy.give_reward()
                hero.recieve_loot(xp,gold,*items)
                return xp,gold,items
            else: 
                draw_lines_aligned(hero.defeat(enemy.name_with_prefix),width=width,pad_over=2,pad_under=3,pause=3)
                return None,None,None