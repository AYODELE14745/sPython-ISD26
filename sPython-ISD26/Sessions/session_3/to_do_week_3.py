# %%
## Section 3: Your first larger-scale Python programme
### Exercise 4: Complete template program

tasks = []
def add_task(task_list):
    task = input("Enter a new task:")
    task_list.append(task)
    print("Task added successfully.")

def view_task(task_list):
    if len(task_list) == 0:
        print("No tasks in the list.")
    else:
        print("\nCurrent Tasks:")
        for index, task in enumerate(task_list, start=1):
            print(index, task)

def remove_task(task_list):
    view_task(task_list)
    if len(task_list) == 0:
        return
    
    try:
        task_number = int(input("Enter the task number to remove:"))
        if 1 <= task_number <= len(task_list):
            remove_task = task_list.pop(task_number - 1)
            print(f"Task '{remove_task}' removed successfully.")
        else:
            print("Task does not exist.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        pass

while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_task(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# %%
