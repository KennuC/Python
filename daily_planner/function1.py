class week:
    def __init__(self, day, tasks):
        self.day = day
        self.tasks = tasks
class task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

# Could try implement a priority queue with task priority

day_library = [
    week("Mon", [
        task("Work", "High")
        ]),
    week("Tue", [
        task("", "")
        ]),
    week("Wed", [
        task("", "")
        ]),
    week("Thu", [
        task("", "")
        ]),
    week("Fri", [
        task("", "")
        ]),
    week("Sat", [
        task("", "")
        ]),
    week("Sun", [
        task("", "")
        ]),
]

def add():
    while True:
        input1 = input("Add to which day: ")
        found_source_day = False
        for day in day_library:
            if day.day == input1:
                found_source_day = True    
                add_task = input("Add what: ")
                add_level = input("Priority level: ")
                new_task = task(add_task, add_level)
                day.tasks.append(new_task)
                return
            elif input1 == "r":
                return
        if not found_source_day:
            print("Invalid day")

def remove():
    while True:
        input1 = input("Remove from which day: ")
        found_source_day = False
        for day in day_library:
            if day.day == input1:
                found_source_day = True
                remove_task = input("Remove what: ")
                for task in day.tasks:
                    if task.description == remove_task:
                        day.tasks.remove(task)
                        break
                else:  
                    print("Task not found")
                return
            elif input1 == "r":
                return
        if not found_source_day:
            print("Invalid day")

def printlist():
    print("__________________________________________")
    for day in day_library:
        print(day.day)
        
        task_with_description = [task for task in day.tasks if task.description]
        for task in task_with_description:
                print(task.description,"-", task.priority)
        print("__________________________________________")
        
printlist()

def move():
    print ("Task to move")
    printlist()
    while True:
        input1 = input("Move from which day: ")
        found_source_day = False
        for day in day_library:
            if day.day == input1:
                found_source_day = True
                move_task = input("Move what: ")
                for task in day.tasks:
                    if task.description == move_task:
                        target_day_input = input("To which day: ")
                        for target_day in day_library:
                            if target_day.day == target_day_input:
                                target_day.tasks.append(task)
                                day.tasks.remove(task)
                                break
                            else:
                                print("Invalid day")
                    elif move_task == "r":
                        return
                    else:
                        print("Invalid task")
            elif input1 == "r":
                return
        if not found_source_day:
            print("Invalid day")