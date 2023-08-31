import Booking
import CheckIn
import CheckOut


def menu():
    print("Welcome to Hilton Hotel")
    while True:
        while True:
            action = input("Book: BK, Check In: CI, Check Out: CO, Exit: EX\n").upper()
            if action in ['BK', 'CI', 'CO', 'EX']:
                break
            else:
                print("Invalid input, please try again.")

        if action == "BK":
            Booking.book_room()
        elif action == "CI":
            CheckIn.check_in()
        elif action == "CO":
            CheckOut.check_out()
        elif action == "EX":
            print("Have a nice day")
            break

if __name__ == "__main__":
    menu()

