import os # Import the os module to allow interacting with the operating system.Example: to check if a file exists.

TASKS_LOG = "daily_tasks_list.txt" # This virable will handle users' tasks that will be saved within daily_tasks_list.txt
print("Your Daily Tasks Manager is Activated!\n All new tasks will be saved to daily_tasks_list.txt file")

#START BULDING THE TASK MANAGER APP
# 1- Define the "Task Manager Menu" function
# 2- Define the "Loading Tasks" function 
# 3- Define the "Saving Tasks" function
# 4- Define the "Adding Tasks" function 
# 5- Define the "Removing Tasks" function


#2 
#define a function named loading_tasks. The function has no parameters because it doesn't require any input when called.
def loading_tasks():
  print("Loading tasks . . .")  # Printing a message showing user that tasks are being loaded.
  if os.path.exists(TASKS_LOG):  # Check if the tasks file exists using os.path.exists within TASKS_LOG > daily_tasks_list.txt file.
    with open(TASKS_LOG, "r") as file:  # Open the file in read mode ("r").
         tasks = file.read().splitlines()  # Read lines and remove extra whitespace
    print(f"{len(tasks)} task/tasks loaded successfully.")  # Print number of loaded tasks.
    return tasks  # Return the list of tasks.
    
  print("No existing task file found.\n***** Starting with an empty task list.*****")  # Message if the statement is false >> file doesn't exist.
  return []  #Return an empty list if the file doesn't exist.



# 3 
# define a function named saving_tasks. 
# The function has parameters because it requires input when called.

def saving_tasks(tasks):        # This Saves tasks to the tasks text file.
    print("Saving tasks . . . ~")  # Print message showing to user that tasks are being saved.
    
    with open(TASKS_LOG, "w") as file:  # Open file in write mode ("w") to enable saving tasks.
        for task in tasks:  # For looping through each task in the list of tasks.
            file.write(task + "\n")  # Write each task to the file followed by a newline.
    
    print("Tasks saved successfully.")  # Print to the user that assigned tasks saved successfully.


#4
def add_task():   #This add a new task to the existing task list
    task = input("Enter task: ")  # Ask the user to input a task.
    tasks = loading_tasks()  # Load the current tasks from the file using the loading_tasks function.
    tasks.append(task)  # Add the new task to the list of tasks.
    saving_tasks(tasks)  # Save the updated list of tasks.
    print(f'Yay! Task "{task}" added successfully.')  # Confirm the user that the new task was added.f'' is a method that print strings besides other data types


#4-B
def list_tasks(): #Showing all tasks.
    print("\nGetting tasks list . . .")  # Print message indicating the task list is being gathered.
    
    tasks = loading_tasks()  # Load the current tasks from the file.
    if tasks:  # Check if the list of tasks isn't empty.
        print("\nYour Tasks:")  # Print a heading for user's list of tasks.
        
        for index, task in enumerate(tasks, 1):  # For loop through the tasks,to get both the index and the task.
            print(f'{index}. {task}')  # Print the task number and the task description.
    else:
        print("*** Opps! No tasks available! ***")  # Print this message if the statement is false, there are no tasks in the list.

#5
def delete_task():  
    print("\nDeleting a task...")  # Indicate task deletion process  
      
    list_tasks()  # Display the current list of tasks  

    task_number = input("\nEnter task number to delete: ")  # Get user input  

    if not task_number.isdigit():  # Check if input is a number  
        print("Error: Please enter a valid numeric task number.")  
        return  #Exit the function directly if the input is invalid.

    task_number = int(task_number)  # Convert input to integer  
    tasks = loading_tasks()  # Load tasks  

    if 1 <= task_number <= len(tasks):  # Tasks List range  
        deleted = tasks.pop(task_number - 1)  # Delete task  
        saving_tasks(tasks)  # Save updated list  
        print(f'Task "{deleted}" deleted successfully.')  
    else:  
        print("*** Opps! Invalid Task Number! *** Please enter a valid task number from the list.")
        return 



#1 
def main(): #Display a menu and process user input.
    app_menu = ["1. Add Task", "2. List Tasks", "3. Delete Task", "4. Exit"]  # Define a list of available menu options.
    
    # For Loop through the options for a maximum of 4 times (or until the user selects 'Exit').
    for _ in range(4):  # The loop runs a maximum of 4 times for user input.
        print("\n**** My Task Manager ****")  # Print a heading for the Task Manager menu.
        
        # Show menu options
        for option in app_menu:  # Loop through each option in the options list.
            print(option)  # Print each menu option (Add Task, List Tasks, Remove Task, Exit).

        usr_choise = input("\nEnter your choice: ")  # Prompt the user to enter their choice from the menu.

        # Process user choice
        if usr_choise == "1":  # Check if the user selected "Add Task".
            add_task()  # Call the add_task function to add a new task.
        elif usr_choise == "2":  # Check if the user selected "List Tasks".
            list_tasks()  # Call the list_tasks function to display the list of tasks.
        elif usr_choise == "3":  # Check if the user selected "Delete Task".
            delete_task()  # Call the remove_task function to delete a task.
        elif usr_choise == "4":  # Check if the user selected "Exit".
            print("Exiting Your Task Manager. See You Soon!")  # Print an exit message.
            break  # Exit the loop and end the App.
        else:
            print("**** Invalid option! ****\nPlease choose a valid option.")  # Printing error message if the user select an invalid option.


# Ensure the script runs only when executed directly.
if __name__ == "__main__":  # This ensures the script runs only when it's executed directly, not when imported.
    main()  # Call the main function to start the Task Manager program.
  


