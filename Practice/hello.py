
class Person:
    def __init__(self, firstName, lastName, favColor):
        self.firstName = firstName
        self.lastName = lastName
        self.favColor = favColor

    def printName(self):
        print("My name is " + self.firstName + " " + self.lastName)


radar = Person("Radar", "Challenger", "red")
kennu = Person("Kennu", "Challenger", "Blue")
Kin = Person("Kin", "Challenger", "red")

radar.printName()
kennu.printName()
Kin.printName()