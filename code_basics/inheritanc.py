import datetime

class Player:
    def __init__(self, name,  username, age, birthYear):
        self.full_name = name
        self.username = username
        self.user_age = age
        self.birth_year = birthYear

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year


class BasketBall(Player):
    def __init__(self, name, username, age, weight, birthYear):
        super().__init__(name, username, age, birthYear)
        self.scores = []
        self.the_weight = weight
        self.birth_year = birthYear

    def add_score(self, score):
        return self.scores.append(score)

    def get_scores_avg(self):
        return sum(self.scores)/len(self.scores)

BPlayer = BasketBall("malik", "AbdMilk", 23, 56, 1988)
BPlayer.add_score(34)
BPlayer.add_score(21)
BPlayer.add_score(15)
print(BPlayer.get_scores_avg())
print(BPlayer.get_age())
print(BPlayer.the_weight)
