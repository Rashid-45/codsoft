tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Added task: {task}")

def list_tasks():
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        print(f"{i + 1}. {task['task']} [{status}]")

def complete_task(task_number):
    if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print(f"Marked task '{tasks[task_number]['task']}' as complete.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Deleted task: {removed_task['task']}")
    else:
        print("Invalid task number.")

# Sample usage
add_task("Finish Python project")
add_task("Review pull request")
list_tasks()
complete_task(0)
list_tasks()
delete_task(1)
list_tasks()
