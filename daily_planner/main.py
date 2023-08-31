import function1

def menu():
    while True:
        while True:
            print("Make a selection")
            action = input("Add: A, Complete: C, Move: M, Show: S\n").upper()
            if action in ['A', 'C', 'M', 'S', 'R']:
                break
            else:
                print("Invalid input, please try again.")

        if action == "A":
            function1.add()
        elif action == "C":
            function1.remove()
        elif action == "M":
            function1.move()
        elif action == "S":
            function1.printlist()
        elif action == "R":
            break
        

if __name__ == "__main__":
    menu()

