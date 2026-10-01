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
    save(save_data)

def read_load() -> Hero:
    s = load()
    return Hero(name=s[0],c_class=s[1],pos=tuple(s[2]),lvl=int(s[3]),gold=int(s[4]))
