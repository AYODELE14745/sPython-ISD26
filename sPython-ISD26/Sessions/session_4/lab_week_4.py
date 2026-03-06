# Classes and Objects
## Section 1: Python Classes
### Exercise 1: Creating Classes and Initializing Object
#%%

class Tasklist:
    def __init__(self, owner):
        self.owner = owner.upper()
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
    
    def remove_task(self, ix):
        if 0 <= ix < len(self.tasks):
            del self.tasks[ix]
            print("Task removed succesfully.")
        else:
            print("Invalid index. No task removed.")
    
    def view_tasks(self, task):
        if not self.tasks:
            print("No tasks available.")
        else:
            print(f"{self.owner}'S TASK LIST:")
            for index, task in enumerate(self.tasks):
                print(f"{index}: {task}")
    
    def list_options(self):
        while True:
            print("To-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Quit")
            
            choice = input("Enter your choice:")
            
            if choice == "1":
                task = input("Enter a task: ")
                self.add_task(task)
                
            elif choice == "2":
                self.view_tasks()
                
            elif choice == "3":
                    ix = int(input("Enter the index of the task to remove:"))
                    self.remove_task(ix)
                
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-4.")

# %%
### Exercise 3: Testing the Functionality
my_task_list = Tasklist("JOSEPH")    
# This part is just to test the functionality by adding some tasks to the list
my_task_list.tasks = ["Do Homework", "Do Laundry", "Go Shopping"]
my_task_list.list_options() 