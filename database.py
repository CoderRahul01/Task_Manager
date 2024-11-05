# database.py
import sqlite3

# Database connection
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Create the tasks table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    status TEXT NOT NULL)''')
conn.commit()

def create_task(title, description, status="pending"):
    """Insert a new task into the database."""
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)", 
                   (title, description, status))
    conn.commit()

def get_task(task_id):
    """Retrieve a task from the database by ID."""
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task_data = cursor.fetchone()
    if task_data:
        return task_data  # Return the tuple directly
    return None

def update_task(task_id, title, description, status):
    """Update an existing task in the database."""
    cursor.execute("UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?",
                   (title, description, status, task_id))
    conn.commit()

def delete_task(task_id):
    """Delete a task from the database by ID."""
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
