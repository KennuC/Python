class Vehicle:
    def __init__(self, name, yearMade, color):
        self.name = name
        self.yearMade = yearMade
        self.color = color
    def forward(self):
        print("Going forward")
    def turnLeft(self):
        print("Turning left")
    def turnRight(self):
        print("Turning right")


class Air(Vehicle):
    def fly(self):
        pass
    def takeoff(self):
        print ("Taking off")

class Ground(Vehicle):
    def breaking(self):
        print ("Breaking")
    def reverse(self):
        print("Going backwards")

    
class Water(Vehicle):
    def submerge(self):
        print ("Going under")
    def anchor(self):
        print("Anchoring")

class plane(Air):
    pass

myPlane = Air(747, 2005, "white")
myPlane.turnLeft()

myBoat = Water("submarine", 2022, "black")
myBoat.submerge()