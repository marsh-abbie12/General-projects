#This is the backend for a to do list app
#Initialise list to store tasks and functions to add and remove tasks
tasks=[] #initialise an empty list to store tasks
def add_task(task): #Add a task to the tasks list
  
    tasks.append(task) 
    return f'Task "{task}" added to the list.'
def remove_task(task): #Remove a task from the tasks list
    tasks.remove(task)
    return f'Task "{task}" removed from the list.'
    
#main programme loop
print("Welcome to the To-DO List App!")
print("You can add tasks, remove tasks, and view your current list of tasks.")
print("Type 'add' to add a task, 'remove' to remove a task, 'view' to view tasks, or 'exit' to exit the app.")

while True:
    task = input("What would you like to do? (add/remove/view/exit): ").lower()
    if task=="view":
        if len(tasks)==0:
            print("Your to-do list is empty.")
        else:
            print("Your current tasks are:")
            for task in tasks:
                print(f"- {task}")
    elif task=="add":
        new_task = input("Enter the task you want to add: ")
        print(add_task(new_task))
    elif task=="remove":
        remove_task_name = input("Enter the task you want to remove: ")
        if remove_task_name in tasks:
            print(remove_task(remove_task_name))
        else:
            print(f'Task "{remove_task_name}" not found in the list.')
    elif task=="exit":
        print("Exiting the To-DO List App. Goodbye!")
        break
    