import random
from collections import Counter

class AI:
    def __init__(self, total_sticks):
        self.hats = {}
        self.chosen = {}
        for item in range(1, total_sticks + 1):
            self.hats[item] = [1, 2, 3]
        for item in self.hats:
            self.chosen[item] = []

    def comp_turn(self, remaining_sticks):
        pick = random.choice(self.hats[remaining_sticks])
        self.chosen[remaining_sticks].append(pick)
        return pick

    def learn_after_win(self):
        for item in self.hats:
            if len(self.chosen[item]) > 0:
                self.hats[item].append(self.chosen[item].pop(0))

    def learn_after_lose(self):
        for item in self.chosen:
            if len(self.chosen[item]) > 0:
                if Counter(self.hats[item])[item] > 1:
                    self.hats[item].remove(item)
