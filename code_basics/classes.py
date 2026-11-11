import datetime
class FootballPlayer:
    def __init__(self, fName, lName, birthYear, team):
        self.first_name = fName
        self.last_name = lName
        self.birth_year = birthYear
        self.team = team
        self.scores = []

    def __str__(self):
        return f"the average score for {self.first_name}, {self.last_name} is approximately {self.get_average()}"

    def add_score(self, score):
        self.scores.append(score)
        return self.scores
    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year
    def get_average(self):
        return sum(self.scores)/len(self.scores)


    #operation overloading, allow oprator behave  for custom object
    def __lt__(self, other):
        self_average_score = self.get_average()
        other_average_score = other.get_average()
        return self_average_score < other_average_score

    def __gt__(self, other):
            self_average_score = self.get_average()
            other_average_score = other.get_average()
            return self_average_score > other_average_score
    
    def __eq__(self, other):
            self_average_score = self.get_average()
            other_average_score = other.get_average()
            return self_average_score == other_average_score
    # def __len__(self):
    #      return self.scores




victor = FootballPlayer("victor", "ibikunle", 1999, "Nigeria")
print(victor.first_name)
print(victor.last_name)
print(victor.birth_year)
print(victor.add_score(56))
print(victor.add_score(67))
print(victor.team)
print(victor.get_age())
print(victor.get_average())
print(victor)
print(len(victor.scores))

Baka = FootballPlayer("mueez", "Bakare", 2999, "Saudi")

print(Baka.add_score(36))
print(Baka.add_score(57))

print(Baka < victor)
print(victor > Baka)
print(victor == Baka)