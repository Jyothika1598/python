import datetime

class Task:
    def __init__(self, title, description="", due_date=None, priority=None, is_completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.is_completed = is_completed

    def __str__(self):
        return f"{self.title} (Due: {self.due_date}, Priority: {self.priority})"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        del self.tasks[index]

    def update_task(self, index, new_title, new_description, new_due_date, new_priority):
        task = self.tasks[index]
        task.title = new_title
        task.description = new_description
        task.due_date = new_due_date
        task.priority = new_priority

    def mark_task_completed(self, index):
        self.tasks[index].is_completed = True

    def mark_task_incomplete(self, index):
        self.tasks[index].is_completed = False

    def get_tasks_by_status(self, status):
        return [task for task in self.tasks if task.is_completed == status]

    def get_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Mark Task Completed")
        print("5. Mark Task Incomplete")
        print("6. View Completed Tasks")
        print("7. View Incomplete Tasks")
        print("8. View Tasks by Priority")
        print("9. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            due_date = input("Enter due date (YYYY-MM-DD, optional): ")
            priority = input("Enter priority (optional): ")
            task = Task(title, description, due_date, priority)
            todo_list.add_task(task)
            print("Task added successfully!")
        elif choice == 2:
            index = int(input("Enter task index to remove: "))
            todo_list.remove_task(index)
            print("Task removed successfully!")
        elif choice == 3:
            index = int(input("Enter task index to update: "))
            new_title = input("Enter new title: ")
            new_description = input("Enter new description (optional): ")
            new_due_date = input("Enter new due date (YYYY-MM-DD, optional): ")
            new_priority = input("Enter new priority (optional): ")
            todo_list.update_task(index, new_title, new_description, new_due_date, new_priority)
            print("Task updated successfully!")
        elif choice == 4:
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_completed(index)
            print("Task marked as completed!")
        elif choice == 5:
            index = int(input("Enter task index to mark as incomplete: "))
            todo_list.mark_task_incomplete(index)
            print("Task marked as incomplete!")
        elif choice == 6:
            completed_tasks = todo_list.get_tasks_by_status(True)
            if completed_tasks:
                print("Completed Tasks:")
                for i, task in enumerate(completed_tasks):
                    print(f"{i+1}. {task}")
            else:
                print("No completed tasks.")
        elif choice == 7:
            incomplete_tasks = todo_list.get_tasks_by_status(False)
            if incomplete_tasks:
                print("Incomplete Tasks:")
                for i, task in enumerate(incomplete_tasks):
                    print(f"{i+1}. {task}")
            else:
                print("No incomplete tasks.")
        elif choice == 8:
            priority = input("Enter priority to filter tasks (optional): ")
            tasks_by_priority = todo_list.get_tasks_by_priority(priority)
            if tasks_by_priority:
                print("Tasks by Priority:")
                for i, task in enumerate(tasks_by_priority):
                    print(f"{i+1}. {task}")
            else:
                print("No tasks with that priority.")
        elif choice == 9:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
