class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def remove_task(self, task_number):
        self.tasks.pop(task_number - 1)

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")

        option = input("\nChoose an option: ")

        if option == "1":
            task = input("\nEnter a task: ")
            todo_list.add_task(task)
        elif option == "2":
            todo_list.view_tasks()
        elif option == "3":
            task_number = int(input("\nEnter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif option == "4":
            break
        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()
