# Project1 - Task Manager

## Overview

This project is a simple console-based **Task Manager** built using Python. The task manager allows you to:

- Create tasks
- List tasks
- Update tasks
- Delete tasks

It uses an **SQLite database** to store tasks persistently. The program runs in a loop and allows interaction via the terminal.

---

## Features

Once the program is running, you can interact with it through commands like:

- **Create** a task
- **List** tasks
- **Update** a task's status
- **Delete** a task
- **Exit** the program

The tasks are stored in an SQLite database called `tasks.db`.

---

## Example Interaction

Here's how the interaction might look like in the terminal:

```bash
Enter command (create, list, update, delete, exit): create
Enter task title: Task 1
Enter task description: This is the first task.
Task 'Task 1' created with ID 1.

Enter command (create, list, update, delete, exit): list
1: Task 1 - pending

Enter command (create, list, update, delete, exit): update
Enter task ID to update: 1
Enter new status (pending, in_progress, completed): in_progress
Task 1 updated to status 'in_progress'.

Enter command (create, list, update, delete, exit): list
1: Task 1 - in_progress

Enter command (create, list, update, delete, exit): delete
Enter task ID to delete: 1
Task 1 deleted.

Enter command (create, list, update, delete, exit): exit
Exiting the task manager.
