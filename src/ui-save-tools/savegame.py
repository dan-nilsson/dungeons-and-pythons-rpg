import os

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

# save()
# print(load())
# clear()
# print(load())