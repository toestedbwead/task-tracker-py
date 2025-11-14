import sys
import json
import os
from datetime import datetime

TASKS_FILE = 'tasks-list.json'

# load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Invalid JSON file. Starting with an empty tasks.")
        return []
    
# save tasks from JSON file

def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")


# main function to handle cli commands
def main():
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [args]")
        return

    command = sys.argv[1]
    tasks = load_tasks()

    if command == 'add':
        if len(sys.argv) < 3:
            print("Error: Please provide a task description.")
            return
        description = sys.argv[2]

        # put a try block here where the user inputs the wrong command

        # generate unique id
        if tasks:
            highest_id = 0
            for task in tasks:
                if task['id'] > highest_id:
                    highest_id = task['id']
            new_id = highest_id + 1
        else:
            new_id = 1


        # create tasks
        now = datetime.now().isoformat()
        new_task = {
        'id': new_id,
        'description': description,
        'status': 'not done',
        'createdAt': now,
        'updatedAt': now
        }

        tasks.append(new_task)
        print(f"Task added succesfully (ID: {new_id})")

        save_tasks(tasks)
    
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Error: Please provide a task id that you want to delete.")
            return
        delete_task_id = int(sys.argv[2]) 


        found_index = -1
        for index, task in enumerate(tasks):
            if task['id'] == delete_task_id:
                found_index = index
                break

        if found_index == - 1:
            print(f"Error: Task with ID {delete_task_id} not found.")
            return 
        

        tasks.pop(found_index)
        print(f"Task deleted succesfully (ID: {delete_task_id} )")

        save_tasks(tasks)

    elif command == 'update':
        if len(sys.argv) < 4:
            print("Error: Please provide a task description.")
            return
        new_updated_task_id = int(sys.argv[2])
        new_description = sys.argv[3]

        found_index = -1
        now = datetime.now().isoformat()
        for index, task in enumerate(tasks):
            if task['id'] == new_updated_task_id:
                task['description'] = new_description
                task['updatedAt'] = now
                found_index = index
                break
        
        if found_index == -1:
            print(f"Error: Task with ID {new_updated_task_id} not found.")
            return
        
        print(f"Task updated succesfully (ID: {new_updated_task_id})")
        save_tasks(tasks)

    
        
        



if __name__ == "__main__":
    main() 
    print("")
    print("CLI Task Tracker Command List:")
    print("")
    print("1. add - create new task")
    print("2. delete - delete task")
    print("3. update - update task description")
    print("4. mark - mark status as done, not done, in progress")
