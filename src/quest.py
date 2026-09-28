class Quest:
    def __init__(self,name,giver,objective,reward):
        self.name = name
        self.giver = giver
        self.objective = objective
        self.reward = reward

    def complete_quest(self,char):
        pass

    def give_reward(self,char):
        pass