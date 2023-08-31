def check_in():
    while True:           
        input1 = input("What is your booking number?\n").upper()
        try:
            with open('booking_number.txt', 'r') as f:
                booking_numbers = f.read().splitlines()
            if input1 in booking_numbers:
                with open('checked_in.txt', 'a') as f:
                    f.write(f"{input1}\n")
                print("Check-in successful. Enjoy your stay")
                return
            else:
                print("No booking found. Please try again.")
        except FileNotFoundError:
            print("No file found. Please try again.")
            break

if __name__ == "__main__":
    check_in()

