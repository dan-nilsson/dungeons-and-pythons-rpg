import os

local_dir = os.path.dirname(__file__)

def save(state=[]):
    savedata = ['test','line1','line2']

    f = open(local_dir+'/.save','w')
    for line in savedata:
        f.write(str(line)+'\n')
    f.close()
    print(local_dir)

def load() -> [str]:
    savedata = []

    f = open(local_dir+'/.save','r')
    f.close()

    return savedata

# save()
# print(load())
