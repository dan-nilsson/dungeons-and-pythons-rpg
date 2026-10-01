import os, time

menu_width = 50
options = ['1. START GAME','2. SAVE GAME ','3. LOAD GAME ','4. CREDITS   ', '5. QUIT GAME ']
side = '#'
splash_ascii = [' ','DUNGEONS &','PYTHONS',' ']
cred = [' ',' ','Daniel Nilsson',' ',' ']

def title_splash():
    draw_lines_centered(splash_ascii)
    time.sleep(2.5)

def menu() -> None:
    draw_lines_centered(options)

def loot_screen(gold,items) -> None:
    draw_lines_centered([f'LOOT:',f'Gold: {gold}','*items'])
    input()

def show_inventory(hero) -> None:
    inv = ['INVENTORY:']+str(hero.inv).splitlines()
    draw_lines_centered(inv,max([len(i) for i in inv])+10)
    input()

def credits_screen() -> None:
    draw_lines_centered(cred)

def screen_clear() -> None:
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def draw_lines_centered(lines,width=menu_width) -> None:
    screen_clear()
    draw_sep(width)
    print(*[side+format_str(width).format(l)+side for l in lines],sep='\n')
    draw_sep(width)

def format_str(width=menu_width) -> str:
    return '{:^'+str(width-2)+'s}'

def draw_sep(width=menu_width) -> None:
    print(f'##{'-'*(width-4)}##')

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

