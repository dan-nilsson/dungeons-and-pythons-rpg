from tools import ( title_splash, loading_screen, menu, credits_screen, draw_sep, screen_clear, invalid_prompt,
                    draw_lines_centered)

def gamemenu(world,hero) -> None:
    while True:

        game_screen()

        match input('Select (1-5) >>> '):
            case '1':
                screen_clear()
                draw_sep()
                name = input('Hero\'s name: ')
                print('Classes: 1. warrior 2. wizard')
                c_class = input('Hero class: ')
                return ['Pythomania'],[name,c_class]
            case '2':
                pass
            case '3':
                pass
            case '4':
                credits_screen()
                input()
            case '5':
                quit()
            case _:
                invalid_prompt()