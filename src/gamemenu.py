from tools import ( game_screen, game_screen_option, invalid_prompt, 
                    attack_splash, loot_screen, show_inventory, cleared_splash)
from combat import fight

def gamemenu(world,hero) -> None:
    had_fight = False
    while True:
        game_screen(world,hero)
        option_str =   (f'{'1. NORTH ' if world.movement_allowed('N') else ''}'+
                        f'{'2. SOUTH ' if world.movement_allowed('S') else ''}'+
                        f'{'3. WEST ' if world.movement_allowed('W') else ''}'+
                        f'{'4. EAST ' if world.movement_allowed('E') else ''}'+
                        f'{'5. MENU'}')
        game_screen_option(option_str)

        if world.current_location().is_hostile: world.add_enemy()
        while world.enemies:
            had_fight = True
            enemy = world.pick_enemy()
            attack_splash(enemy)
            xp,gold,item = fight(hero,enemy)
            if not hero.is_alive: return
            loot_screen(xp,gold,item)
            show_inventory(hero)
        if had_fight:
            cleared_splash(world.current_location())
            game_screen(world,hero)
            game_screen_option(option_str)
            had_fight = False

        match input('Select (1-5) >>> '):
            case '1':
                if world.movement_allowed('N'): world.move('N')
            case '2':
                if world.movement_allowed('S'): world.move('S')
            case '3':
                if world.movement_allowed('W'): world.move('W')
            case '4':
                if world.movement_allowed('E'): world.move('E')
            case '5':
                return
            case _:
                invalid_prompt()