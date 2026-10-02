from tools import ( title_splash, loading_screen, menu_screen, credits_screen, invalid_prompt,
                    draw_sep, screen_clear, draw_lines_aligned)
from savegame import create_save, read_load, clear
from hero import Hero
from gameworld import GameWorld

def mainmenu(active=False,in_game=None,in_hero=None):
    select = 0
    active_game = active
    game = in_game
    hero = in_hero

    while True:
        if not active_game:
            title_splash()
            loading_screen()
            active_game = True
    
        menu_screen()

        match input('Select (1-5) >>> '):
            case '1':
                screen_clear()
                draw_sep()
                name = input('Hero\'s name: ')
                print('Classes: 1. warrior 2. wizard')
                c_class = input('Hero class: ')
                return GameWorld('Pythomania'),Hero(name,c_class),True
            case '2':
                if hero: 
                    create_save(hero)
                    draw_lines_aligned(['GAME SAVED'],pad_over=3,pad_under=3)
                    input()
                else:
                    draw_lines_aligned(['NO GAME TO SAVE'],pad_over=3,pad_under=3)
                    input()
            case '3':
                try:
                    hero = read_load()
                    game = game if game else GameWorld('Pythomania')
                except OSError:
                    draw_lines_aligned(['NO GAME TO LOAD'],pad_over=3,pad_under=3,pause=2)
                if game and hero:
                    draw_lines_aligned(['GAME LOADED'],pad_over=3,pad_under=3)
                    input()
                    return game,hero,True
                else:
                    return None,None,None
            case '4':
                credits_screen()
                input()
            case '5':
                quit()
            case _:
                invalid_prompt()