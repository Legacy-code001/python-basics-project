tasks = []


while True:
    print("To Do List Menu")
    print("1. Add Task")
    print("2. view all task")
    print("3. Remove a task")
    print("4. Quit")

    select_task = input("select task to perform(add, view, remove, quit): ").strip().lower()

    if select_task == "add" or select_task == "1":
        the_task = input("enter the task description: ").strip()
        if the_task:
            tasks.append(the_task)
            print(f"the {the_task} added succefully")
        else:
            print("the task description cannot be empty")
        
    elif select_task == "view" or select_task == "2":
        if not tasks:
            print("you to-do list is currently empty")
        else:
            for index, val in enumerate(tasks, start=1):
                print(f"{index}. {val}")
    elif select_task == "remove" or  select_task == "3":
        if not tasks:
            print("there is no available task to remove")
        else:
            for index, val in enumerate(tasks, start=1):
                print(f"{index}. {val}")

            try:
                task_to_remove = int(input(f"input the task number to remove: "))
                if 1 <= task_to_remove <= len(tasks):
                    removed = tasks.pop(task_to_remove - 1)
                    print(f"Remove task {removed}")
                else:
                    print("ivalid selection, task number does not exit")
            except ValueError:
                print("please enter valid numeric number")
    elif select_task == "quit" or select_task == "4":
        print("Goodby for now")
        break
    else:
        print("invalid option, please select task from add, view, remove or quit")









