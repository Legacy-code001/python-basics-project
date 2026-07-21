# defining the class

class Human:
    def __init__ (self, n, o):
        self.name = n
        self.occupation = o
    def do_work(self):
        if self.occupation == "footballer":
            print(self.name,"is a player")
    def speak(self):
        if self.name == "raheem":
            print(self.name, "yes, he can speak")
        else:
            print("its not correct")
    def walks(self):
       print(self.name + " walks home everyday")


# instntite
mueez = Human("raheem", "footballer")

mueez.do_work()
mueez.speak()
mueez.walks()