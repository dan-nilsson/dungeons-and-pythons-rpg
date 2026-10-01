from tools import game_screen, game_screen_option, invalid_prompt

def gamemenu(world,hero) -> None:
    while True:

        game_screen(world,hero)
        game_screen_option()

        match input('Select (1-5) >>> '):
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '5':
                return
            case _:
                invalid_prompt()