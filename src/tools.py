import os, time, random

menu_width = 50
options = ['DUNGEONS & PYTHONS','1. START GAME','2. SAVE GAME ','3. LOAD GAME ','4. CREDITS   ', '5. QUIT GAME ']
side = '#'
splash_ascii = ['DUNGEONS &','PYTHONS']
cred = ['Daniel Nilsson']
filled,empty,end = '█','_','|'

def title_splash():
    draw_lines_centered(splash_ascii,pad_over=2,pad_under=2)
    time.sleep(2.5)

def menu() -> None:
    draw_lines_centered(options)

def loot_screen(xp,gold,items) -> None:
    items = [str(i) for i in items]
    draw_lines_centered([f'REWARDS:',f'XP: {xp}',f'GOLD: {gold}',]+items,max([len(i) for i in items])+10,
                        pad_over=1,pad_under=1)
    input()

def show_inventory(hero) -> None:
    inv = ['INVENTORY:']+str(hero.inv).splitlines()
    draw_lines_centered(inv,max([len(i) for i in inv])+10,pad_over=1,pad_under=1)
    input()

def credits_screen() -> None:
    draw_lines_centered(cred,pad_over=2,pad_under=2)

def loading_screen() -> None:
    loading = 0
    while loading < 100:
        num_load= round((loading / 100)*20)
        num_notload = 20 - num_load
        load_bar = f'{end}{filled * num_load}{empty * num_notload}{end}'
        draw_lines_centered(['LOADING',load_bar],pad_over=2,pad_under=2)
        loading += 10
        time.sleep(random.uniform(0.1,0.4))

def invalid_prompt() -> None:
    draw_lines_centered(['Invalid Selection'],pad_over=2,pad_under=3)

def screen_clear() -> None:
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def draw_lines_centered(lines,width=menu_width,pad_over=0,pad_under=0,pause=0) -> None:
    screen_clear()
    draw_sep(width,empty_under=pad_over)
    print(*[draw_line(l,width) for l in lines],sep='\n')
    draw_sep(width,empty_over=pad_under)
    time.sleep(pause)

def draw_line(line='',width=menu_width) -> str:
    return side+('{:^'+str(width-2)+'s}').format(line)+side

def draw_line_left(line='',width=menu_width) -> str:
    return side+('{:<'+str(width-2)+'s}').format(line)+side

def draw_sep(width=menu_width,empty_over=0,empty_under=0) -> None:
    if empty_over: print(*[draw_line(width=width)]*empty_over,sep='\n')
    print(f'##{'-'*(width-4)}##')
    if empty_under: print(*[draw_line(width=width)]*empty_under,sep='\n')

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

