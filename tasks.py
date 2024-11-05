# tasks.py
class Task:
    def __init__(self, title, description):
        self.id = None  # Will be set when the task is saved to the DB
        self.title = title
        self.description = description
        self.status = "pending"  # Default status

    def update_status(self, new_status):
        if new_status in ["pending", "in_progress", "completed"]:
            self.status = new_status
        else:
            print("Invalid status!")

    def __str__(self):
        return f"{self.id}: {self.title} - {self.status}"
