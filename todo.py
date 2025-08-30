# To Do List Code CLI :

tasks = []

while True:
    print("\n-- To Do List Menu --")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        while True:
           task = input("Enter Task: ")
           tasks.append(task)
           print(f"Task '{task}' Successfully Added ✅")

           again = input("Do you want to continue? (y/n): ").lower() # continue in the current append loop.
           if again =="y":
             continue
           elif again == "n":
             break
           else:
            print("Invalid Identifier ❌")

    elif choice == "2":
        if not tasks:
            print("\nNo tasks found ☹️")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove ☹️")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_nums = input("Enter task numbers to remove (Use Comma Separated Values): ")
            try:
                indexes = [int(x.strip()) for x in task_nums.split(",")]
                indexes.sort(reverse=True)

                for task_num in indexes:
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"Task '{removed_task}' removed ✅")
                    else:
                        print(f"Task number {task_num} not found ☹️")
            except ValueError:
                print("Invalid input! Please enter numbers only.")

    elif choice == "4":
        print("Goodbye, Have a nice day dear 😊😊")
        break

    else:
        print("Invalid Choice, please try again ❌")
