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

    match input('Make Selection (1-5) >>> '):
        case '1':
            screen_clear()
            name = input('Enter your hero\'s name: ')
            c_class = input('Pick Class 1.Warrior 2.Wizard: ')
        case '2':
            if save_data: 
                save(save_data)
                print('GAME SAVED')
                input()
            else:
                print('No game progress to save.')
                input()
        case '3':
            save_data = load()
            if not save_data: print('No data to load.')
            else: print('GAME STARTING')
            input()
        case '4':
            credits_screen()
            input()
        case '5':
            quit()
        case _:
            screen_clear()
            print('\n\n  Invalid selection.')
            time.sleep(2)