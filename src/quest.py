import objective

class Quest:
    def __init__(self,name,giver='f00',objective=None,reward=(200,200)):
        self.name = name
        self.giver = giver
        self.objective = objective if objective else Objective()
        self.reward = reward

    def complete_quest(self,char):
        give_reward()
        print(  f'Quest {self.name} completed!\n'+
                f'Reward: {reward[0]}XP and {reward[1]}gold')

    def give_reward(self,char):
        char.gain_xp(self.reward[0])
        char.gold += reward[1]