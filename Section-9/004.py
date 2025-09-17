# self args
class Chaicup:
    size = 150 # ml

    # method, in all the methods 
    def describe(self):
        return f"A {self.size} ml chai cup!"
    
cup = Chaicup()
print(cup.describe())

print(Chaicup.describe(cup))
