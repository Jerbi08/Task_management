class Task:
    def __init__(self, id, title, description, assignee, status="Pending"):
        self.id = id
        self.title = title
        self.description = description
        self.assignee = assignee
        self.status = status
    
    def mark_complete(self):
        self.status = "Completed"
    
    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nAssignee: {self.assignee}\nStatus: {self.status}\n"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add_task(self, title, description, assignee):
        task = Task(self.next_id, title, description, assignee)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def assign_task(self, task_id, new_assignee):
        for task in self.tasks:
            if task.id == task_id:
                task.assignee = new_assignee
                return True
        return False
    
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                return True
        return False
    
    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def list_tasks(self, status=None):
        if status:
            return [task for task in self.tasks if task.status == status]
        return self.tasks
    
    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                return self.tasks.pop(i)
        return None

def main():
    manager = TaskManager()
    
    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. Assign Task to someone else")
        print("3. Mark Task as Complete")
        print("4. View All Tasks")
        print("5. View Pending Tasks")
        print("6. View Completed Tasks")
        print("7. Delete Task")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            assignee = input("Enter assignee name: ")
            task = manager.add_task(title, description, assignee)
            print(f"Task added successfully!\n{task}")
        
        elif choice == "2":
            task_id = int(input("Enter task ID to reassign: "))
            new_assignee = input("Enter new assignee name: ")
            if manager.assign_task(task_id, new_assignee):
                print("Task reassigned successfully!")
            else:
                print("Task not found!")
        
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as complete: "))
            if manager.complete_task(task_id):
                print("Task marked as complete!")
            else:
                print("Task not found!")
        
        elif choice == "4":
            tasks = manager.list_tasks()
            if tasks:
                print("\nAll Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks found!")
        
        elif choice == "5":
            tasks = manager.list_tasks(status="Pending")
            if tasks:
                print("\nPending Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No pending tasks found!")
        
        elif choice == "6":
            tasks = manager.list_tasks(status="Completed")
            if tasks:
                print("\nCompleted Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No completed tasks found!")
        
        elif choice == "7":
            task_id = int(input("Enter task ID to delete: "))
            task = manager.delete_task(task_id)
            if task:
                print(f"Task deleted successfully!\n{task}")
            else:
                print("Task not found!")
        
        elif choice == "8":
            print("Exiting Task Management System, Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
