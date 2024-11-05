# ui.py

def print_tasks(tasks):
    """Print a list of tasks."""
    if not tasks:
        print("No tasks to display.")
        return
    for task in tasks:
        print(task)

def get_user_input():
    """Prompt the user for a command."""
    user_input = input("Enter command (create, list, update, delete, exit): ").lower()
    return user_input
