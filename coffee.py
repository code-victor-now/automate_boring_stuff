class Cofee:
    def __init__(self):
        self.content = 1.0
    def drink(self):
        self.content = 0.0
        
cup = Cofee()

print (cup.content)

cup.drink()

print (cup.content, "Nice Cofee!")
