def task():
    tasks = [] #empty list
    print("\n----WELCOME TO THE TASK MANAGEMENT APP----\n")

    total_tasks = int(input("Enter number of tasks you want to add : "))

    for i in range(1,total_tasks+1):
        task_name = input(f"Enter your Task {i} : ")
        tasks.append(task_name)

    print(f"Your tasks are : \n{tasks}")

    while True: 
        operation = int(input("Enter to perform : \n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\nEnter number : "))
        if operation == 1:
            add = input("Enter task you want to add : ")
            tasks.append(add)
            print(f"Task {add} has been added successfully...")

        elif operation == 2:
            old_task = input("Enter task you want to upadate : ")
            if old_task in tasks: 
                new_task = input("Enter new task : ")
                index = tasks.index(old_task)
                tasks[index] = new_task
                print(f"Updated task {new_task} has been updated...")

        elif operation == 3: 
            del_task = input("Enter the tast you want to delete : ")
            if del_task in tasks:
                index = tasks.index(del_task)
                del tasks[index]
                print(f"Your task {del_task} has been deleted...")

        elif operation == 4:
            print(f"Your tasks are : \n{tasks}")

        elif operation == 5:
            print("Closing the programme...")
            break

        else: 
            print("Invalid Input")



task()    

