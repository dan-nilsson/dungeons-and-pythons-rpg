class Hero(Character):
    def __init__(self,name,pos,life,equip,lvl,c_class,inv,quests):
        super().__init__(name,pos,life,equip,lvl)
        self.c_class = c_class
        self.inv = inv
        self.quests = quests

    def accept_quest(self,quest):
        self.quests.append(quest)

    def get_inventory(self):
        pass

    def equip_item(self):
        pass