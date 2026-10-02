'''
Didn't end up using.
'''

standard_desc = 'Kill 1 Boar'

class Objective:
    def __init__(self,desc=standard_desc,count=1):
        self.desc = desc
        self.count = count
        self.current_count = 0

    def progress_obj(self,amount):
        self.current_count += amount
        if current_count >= count: obj_completed()

    def obj_completed(self):
        print(f'Objective: {self.desc} completed.')