import os

from hero import Hero

local_dir = os.path.dirname(__file__)

def save(state=[],clear=False):
    savedata = ['test','line1','line2'] if not state else state

    f = open(local_dir+'/.save','w')
    if clear: pass
    else:
        for line in savedata:
            f.write(str(line)+'\n')
    f.close()

def load() -> [str]:
    f = open(local_dir+'/.save','r')
    state = f.read().splitlines()
    f.close()

    return state

def clear():
    save(clear=True)

def create_save(hero):
    save_data =[hero.name,
                hero.c_class,
                str(hero.pos),
                str(hero.lvl.lvl),
                str(hero.gold)]
    try: save(save_data)
    except OSError: print('No write permission.')

def read_load() -> Hero:
    try: s = load()
    except OSError: print('File not found.')
    return Hero(name=s[0],c_class=s[1],pos=tuple(s[2]),lvl=int(s[3]),gold=int(s[4]))
