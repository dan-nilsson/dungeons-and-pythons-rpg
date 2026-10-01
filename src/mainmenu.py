import os, time

from tools import ( title_splash, loading_screen, menu, credits_screen, draw_sep, screen_clear, invalid_prompt,
                    draw_lines_centered)
from savegame import save, load, clear

def mainmenu(active=False) -> None:
    select = 0
    active_game = active
    save_data = []

    while not select:
        if not active_game:
            title_splash()
            loading_screen()
            
        active_game = True

        menu()

        match input('Select (1-5) >>> '):
            case '1':
                screen_clear()
                draw_sep()
                name = input('Hero\'s name: ')
                print('Classes: 1. warrior 2. wizard')
                c_class = input('Hero class: ')
                return ['Pythomania'],[name,c_class]
            case '2':
                if save_data: 
                    save(save_data)
                    draw_lines_centered(['GAME SAVED'],pad_over=3,pad_under=3)
                    input()
                else:
                    draw_lines_centered(['NO GAME TO SAVE'],pad_over=3,pad_under=3)
                    input()
            case '3':
                save_data = load()
                if not save_data: draw_lines_centered(['NO GAME TO LOAD'],pad_over=3,pad_under=3,pause=2)
                else:
                    return ['Pythomania'],['LoadName','warrior']
            case '4':
                credits_screen()
                input()
            case '5':
                quit()
            case _:
                invalid_prompt()
                time.sleep(1)