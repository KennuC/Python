from random import randint


class Room:
    def __init__(self, level, number, price):
        self.level = level
        self.number = number
        self.price = price
    
    def printInput(self):
        print("Level: " + self.level + " " + "Room: " + self.number + " " + "Price: " + self.price + "/Night")

room_library = [
    Room("1", "101", "$100"),
    Room("1", "102", "$100"),
    Room("1", "103", "$100"),
    Room("2", "201", "$500"),
    Room("2", "202", "$500"),
    Room("2", "203", "$500"),
    Room("3", "301", "$1000"),
    Room("3", "302", "$1000"),
    Room("3", "303", "$1000")
]

def book_room():
       while True: 
            room = None
            price = 0
            while True:
                action = input("What room level would you like?\nRegular: R, Family: F, Penthouse: P\n").upper()
                if action in ['R', 'F', 'P']:
                    break
                else:
                    print("Invalid input, please try again.")

            if action == "R":
                room = room_library[0]
            elif action == "F":
                room = room_library[3]
            elif action == "P":
                room = room_library[6]

            if room is not None:
                room.printInput()
                price = int(room.price.strip('$'))
            else:
                print("Invalid input, returning")
                return

            while True:
                try:
                    value = int(input("How many nights?\n"))
                    if value > 0:
                        break
                    else:
                        print("Invalid input, please enter a positive number.")
                except ValueError:
                    print("Invalid input, please enter a number.")

            total = value * price
            print(f"This will cost a total of: ${total} for {value} nights")

            while True:
                confirm = input("Do you want to confirm booking?\nYes: Y, No: N\n").upper()
                if confirm in ['Y', 'N']:
                    break
                else:
                    print("Invalid input, please try again.")

            if confirm == "Y":
                booking_numbers = randint(1,999)
                print(f"Booking confirmed for {value} nights. Your booking number is {booking_numbers}.")
                with open('C:/Users/kennu/OneDrive/Documents/programming/Python/Hotel/booking_number.txt', 'a') as f:
                    f.write(f"{booking_numbers}\n")
                break
            elif confirm == "N":
                print("Returning")
                

if __name__ == "__main__":
    book_room()