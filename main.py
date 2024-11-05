# main.py
import tasks
import database
import task_ui

def main():
    tasks_list = []

    while True:
        user_input = task_ui.get_user_input()

        if user_input == "create":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = tasks.Task(title, description)
            # Call database.create_task with title and description instead of the task object
            database.create_task(task.title, task.description, task.status)
            tasks_list.append(task)
            print(f"Task '{task.title}' created with ID {task.id}.")

        elif user_input == "list":
            task_ui.print_tasks(tasks_list)

        elif user_input == "update":
            task_id = int(input("Enter task ID to update: "))
            task = database.get_task(task_id)
            if task:
                task_obj = tasks.Task(task[1], task[2])
                task_obj.id = task[0]
                task_obj.status = task[3]
                new_status = input("Enter new status (pending, in_progress, completed): ")
                task_obj.update_status(new_status)
                database.update_task(task_obj.id, task_obj.title, task_obj.description, task_obj.status)
                print(f"Task {task_obj.id} updated to status '{task_obj.status}'.")
            else:
                print(f"Task with ID {task_id} not found.")

        elif user_input == "delete":
            task_id = int(input("Enter task ID to delete: "))
            task = database.get_task(task_id)
            if task:
                database.delete_task(task_id)
                tasks_list = [t for t in tasks_list if t.id != task_id]
                print(f"Task {task_id} deleted.")
            else:
                print(f"Task with ID {task_id} not found.")

        elif user_input == "exit":
            print("Exiting the task manager.")
            break

        else:
            print("Invalid command. Please enter 'create', 'list', 'update', 'delete', or 'exit'.")

if __name__ == "__main__":
    main()
