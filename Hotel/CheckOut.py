def check_out():
    while True:           
        input1 = input("What is your booking number?\n").upper()
        try:
            with open('C:/Users/kennu/OneDrive/Documents/programming/Python/Hotel/checked_in.txt', 'r') as f:
                booking_numbers = f.read().strip().split()
            if input1 in booking_numbers:
                while True:
                    confirm = input("Confirm Check-Out?\nYes: Y, No: N\n").upper()
                    if confirm in ['Y', 'N']:
                        break
                    else:
                        print("Invalid input, please try again.")
                if confirm == "Y":
                    booking_numbers.remove(input1)
                    with open('C:/Users/kennu/OneDrive/Documents/programming/Python/Hotel/checked_in.txt', 'w') as f:
                        f.write('\n'.join(booking_numbers))
                    with open('C:/Users/kennu/OneDrive/Documents/programming/Python/Hotel/booking_number.txt', 'w') as f:
                        f.write('\n'.join(booking_numbers))
                    print("Thank You for choosing Hilton Hotel")
                    break
                elif confirm == "N":
                    print("Returning")        
            else:
                print("No booking found. Please try again.")
        except FileNotFoundError:
            print("No file found. Please try again.")
            break


if __name__ == "__main__":
    check_out()

