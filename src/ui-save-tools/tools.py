import os, time

menu_width = 50
format_str = '{:^'+str(menu_width-2)+'s}'
options = ['1. START GAME','2. LOAD GAME ','3. CREDITS   ', '4. QUIT GAME ']
side = '#'
line = f'##{'-'*(menu_width-4)}##'
splash_ascii = [' ','DUNGEONS &','PYTHONS',' ']
cred = [' ',' ','Daniel Nilsson',' ',' ']

def title_splash():
    draw_lines_centered(splash_ascii)
    time.sleep(2.5)

def menu() -> None:
    draw_lines_centered(options)

def credits_screen() -> None:
    draw_lines_centered(cred)

def screen_clear() -> None:
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

def draw_lines_centered(lines) -> None:
    screen_clear()
    draw_sep()
    print(print(*[side+format_str.format(l)+side for l in lines if l],sep='\n'))
    draw_sep()

def draw_sep() -> None:
    print(line)

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

