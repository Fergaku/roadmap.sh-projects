# Create a task manager that allows you to add, delete, mark as done, and view tasks.

import time
import datetime
tasks= {}
task_counter= 1
# Format: {task1: [description, status]}
print('Welcome to the task manager!')
time.sleep(1.2)
print('Choose what you want to do.')
try:
    print('1. Add task')
    print('2. Update task')
    print('3. Delete task')
    print('4. Mark task')
    print('5. View tasks')
    print('Press any other key to exit.')
    choice = int(input())
except ValueError: # Activates if user enters a string.
    print('Invalid choice. Please enter a valid number.')
    choice = int(input())
except KeyboardInterrupt: # Activates if user interrupts the program. (Crtl + C)
    print('Program interrupted by user!')
    exit()
    
while True:
    if choice == 1:
        # Add task
        new_task=input('Add a task:\n') # Ask the user to input a task.
        new_task_description=input('Add a description:\n') # Ask the user to input a description for the task.
        current_time = datetime.datetime.now()
        task_id= f'Task {task_counter}'
        tasks[task_id]={'name': new_task,
                        'description': new_task_description,
                         'status': '',
                         'date created': current_time} # The following dictionary shows the structure of the new task.
        print(f"{task_id} added!")
        task_counter+=1
        
    # Update task
    elif choice == 2:
        choice_update = input('Which task do you want to update?\n') # Ask the user to input an existing task.
        if choice_update in tasks:
            new_task_description=input('Update the description:')
            tasks[choice_update]=new_task_description
            print('Task updated!')
        else:
            print(f"task {choice_update} not found.")
        
    # Delete task
    elif choice == 3:
        print('Which task do you want to delete?')
        choice_delete = input()
        if choice_delete in tasks:
            tasks.pop(choice_delete)
            print('Task deleted!')
        else:
            print(f"task {choice_delete} not found.")
        
    # Mark task
    elif choice == 4:
        if not tasks:
            print('No tasks available!')
        else:
            print('Choose the task you want to mark:')
            choice_mark = input()
            if choice_mark in tasks:
                print('Choose the status of the task:')
                print('1. In progress')
                print('2. Done')
                choice_status = int(input())
                match choice_status:
                    case 1:
                        tasks[choice_mark]['status'] = 'In progress'
                    case 2:
                        tasks[choice_mark]['status'] = 'Done'
                print(f"Task marked as: {tasks[choice_mark]['status']}")
    
    # Observe all tasks                
    elif choice == 5:
        print('Choose between the types')
        print('1. All tasks')
        print('2. Tasks in progress')
        print('3. Done tasks')
        choice_5 = int(input())
        
        match choice_5:
            case 1:
                print('All tasks')
                for task, details in tasks.items():
                    print(f"{details['name']}")
                    print(f"Description: {details['description']}")
                    print(f"STATUS: {details['status']}\n")
            case 2:
                print('Tasks in progress')
                for task, status in tasks.items(): 
                    if details['status'] == 'In progress':
                        print(f"{details['name']}")
                        print(f"Description: {details['description']}")
                        print(f"STATUS: {details['status']}\n")
            case 3:
                print('Done tasks')
                for task, status in tasks.items(): 
                    if details['status'] == 'Done':
                        print(f"{details['name']}")
                        print(f"Description: {details['description']}")
                        print(f"STATUS: {details['status']}\n")
    else: # If the user chooses any other key, the program will exit.
        print('Goodbye!')
        break
    
    time.sleep(1.2)
    try:
        print('1. Add another task')
        print('2. Update task')
        print('3. Delete task')
        print('4. Mark task')
        print('5. View tasks')
        print('Press any other key to exit.')
        choice = int(input())
    except ValueError: # If the user adds a string, the program will ask for a valid number.
        print('Invalid choice. Please enter a valid number.')
        choice = int(input())
    except KeyboardInterrupt: # If the user interrupts the program, the program will exit.
        print('Program interrupted by user!')
        break