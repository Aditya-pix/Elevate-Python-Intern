import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.txt")

# Ensure tasks.txt exists when program starts
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "w") as f:
        pass  


def load_tasks():
    """Load tasks from file if exists"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return [line.strip() for line in f.readlines()]
    return []

def save_tasks(todo):
    """Save tasks to file"""
    with open(TASKS_FILE, "w") as f:
        for task in todo:
            f.write(task + "\n")

def add(task, todo):
    todo.append(task)
    save_tasks(todo)

def remove(task, todo):
    if task not in todo:
        print("Task not added previously!!!")
    else:
        todo.remove(task)
        save_tasks(todo)

def view(todo):
    if len(todo) == 0:
        print("Nothing in todo list")
    else:
        for i, task in enumerate(todo, start=1):
            print(f"{i}. {task}")

def todo_app():
    print('---> To Do App <---\n')
    todo = load_tasks()

    while True:
        print(" ---- Menu ---- \n")
        print("1. Add")
        print("2. Remove")
        print("3. View")
        print("4. Exit")
        
        choice = input("\nEnter choice (1-4): ")

        if choice == '4':
            print("Exiting To Do App. Goodbye!")
            break

        if choice not in ('1', '2', '3'):
            print("Invalid choice, try again.")
            continue

        match choice:
            case '1':
                task = input("Enter your task: ").strip()
                if task:
                    add(task, todo)
                    print("Task added Successfully!")
            case '2':
                task = input("Enter task to remove: ").strip()
                remove(task, todo)
            case '3':
                view(todo)

if __name__ == '__main__':
    todo_app()
