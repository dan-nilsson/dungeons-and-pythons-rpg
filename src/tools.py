import os, time, random

menu_width = 50
options = ['DUNGEONS & PYTHONS','1. START GAME','2. SAVE GAME ','3. LOAD GAME ','4. CREDITS   ', '5. QUIT GAME ']
# game_options = '1. N    2. S    3. W    4. E    5. MENU'
side = '#'
splash_ascii = ['DUNGEONS &','PYTHONS']
cred = ['Daniel Nilsson']
filled,empty,end = '█','_','|'

def title_splash():
    draw_lines_aligned(splash_ascii,pad_over=2,pad_under=2)
    time.sleep(2)

def menu_screen() -> None:
    draw_lines_aligned(options)

def loot_screen(xp,gold,items) -> None:
    items = [str(i) for i in items if i] if items else ['']
    draw_lines_aligned([f'REWARDS:',f'XP: {xp}',f'GOLD: {gold}',]+items,max([len(i) for i in items])+10,
                        pad_over=1,pad_under=1)
    input()

def show_inventory(hero) -> None:
    inv = ['INVENTORY:']+str(hero.inv).splitlines()
    draw_lines_aligned(inv,max([len(i) for i in inv])+10,pad_over=1,pad_under=1)
    input()

def credits_screen() -> None:
    draw_lines_aligned(cred,pad_over=2,pad_under=2)

def loading_screen() -> None:
    loading = 0
    while loading < 100:
        num_load= round((loading / 100)*20)
        num_notload = 20 - num_load
        load_bar = f'{end}{filled * num_load}{empty * num_notload}{end}'
        draw_lines_aligned(['LOADING',load_bar],pad_over=2,pad_under=2)
        loading += 10
        time.sleep(random.uniform(0.1,0.4))

def attack_splash(enemy) -> None:
    draw_lines_aligned([f'{enemy.name} has attacked you.'],menu_width,pad_over=2,pad_under=3,pause=3)

def cleared_splash(location) -> None:
    draw_lines_aligned([f'{location.name_with_prefix()} has been cleared','of all foes!'],menu_width,pad_over=2,pad_under=2,pause=3)

def invalid_prompt() -> None:
    draw_lines_aligned(['Invalid Selection'],pad_over=2,pad_under=3,pause=1)

def game_screen(world,hero) -> None:
    width = menu_width+10
    loc = world.current_location()
    loc =  (f'LOCATION : {loc.name_with_prefix()} {loc.biome.capitalize()} '+
            f'{'[Hostile]' if loc.is_hostile else '[Safe]'}')
    lines =[f'NAME : {hero.name}',
            f'HEALTH: {hero.hp_bar.draw(onlybar=True,cust_len=20)} {hero.life} / {hero.max_life}',
            f'LVL: {hero.lvl.lvl}   ( {hero.lvl.current_xp} / {hero.lvl.xp_per_level} XP )',
            f'{str(hero.equipped_wep())}', 
            f'GOLD: {hero.gold}g',
            f'INV: {hero.inv.inventory_status()} slots used.']
    screen_clear()
    draw_sep(width)
    print(draw_line_center(loc,width))
    draw_lines_aligned(lines,width,align='left',pad_side=3,clear=False)

def game_screen_option(game_options):
        print(draw_line_center(game_options,menu_width+10))
        draw_sep(menu_width+10)

def screen_clear() -> None:
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

'''
General drawing functions for UI-elements. clears screen. Paints the contents within borders.
Aligned to left or centered. With padding for empty bordered lines and pause for time.sleep().
'''
def draw_lines_aligned( lines,width=menu_width,align='center',
                        pad_side=0,pad_over=0,pad_under=0,pause=0,clear=True) -> None:
    if clear: screen_clear()
    draw_sep(width,empty_under=pad_over)
    if align == 'center': print(*[draw_line_center(l,width) for l in lines],sep='\n')
    if align == 'left': print(*[draw_line_left((' '*pad_side)+l,width) for l in lines],sep='\n')
    draw_sep(width,empty_over=pad_under)
    time.sleep(pause)

def draw_line_center(line='',width=menu_width) -> str:
    return side+('{:^'+str(width-2)+'s}').format(line)+side

def draw_line_left(line='',width=menu_width) -> str:
    return side+('{:<'+str(width-2)+'s}').format(line)+side

def draw_sep(width=menu_width,empty_over=0,empty_under=0) -> None:
    if empty_over: print(*[draw_line_center(width=width)]*empty_over,sep='\n')
    print(f'##{'-'*(width-4)}##')
    if empty_under: print(*[draw_line_center(width=width)]*empty_under,sep='\n')

'''
  ____                                            ___
 |  _ \ _   _ _ __   __ _  ___  ___  _ __  ___   ( _ )
 | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \/ __|  / _ \/\
 | |_| | |_| | | | | (_| |  __/ (_) | | | \__ \ | (_>  <
 |____/ \__,_|_| |_|\__, |\___|\___/|_| |_|___/ \___/\/
          ____      |___/ _
         |  _ \ _   _| |_| |__   ___  _ __  ___
         | |_) | | | | __| '_ \ / _ \| '_ \/ __|
         |  __/| |_| | |_| | | | (_) | | | \__ \
         |_|    \__, |\__|_| |_|\___/|_| |_|___/
                |___/
'''

