import os, time

from tools import title_splash, menu, screen_clear, credits_screen
from savegame import save, load, clear

select = None
active_game = None
save_data = []

while not select:
    if not active_game: title_splash()
    active_game = 1
    
    menu()
    inp = input('Make Selection (1-4) >>> ')

    match inp:
        case '1':
            screen_clear()
            print('GAME STARTING')
            input()
        case '2':
            save_data = load()
            if not save_data: print('No data to load.')
            else: print('GAME STARTING')
            input()
        case '3':
            credits_screen()
            input()
        case '4':
            quit()
        case _:
            screen_clear()
            print('\n\n  Invalid selection.')
            time.sleep(2)
            screen_clear()