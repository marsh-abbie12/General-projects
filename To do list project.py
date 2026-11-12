#This is the backend for a to do list app
tasks=[] #initialise an empty list to store tasks
def add_task(task):
    #Add a task to the tasks list
    tasks.append(task)
    return f'Task "{task}" added to the list.'
def remove_task(task):
    tasks.remove(task)
    return f'Task "{task}" removed from the list.'
    #Remove a task from the tasks list
