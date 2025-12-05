#!/usr/bin/env python3
"""
Simple To-Do List (Pure Python)
- Add tasks
- View tasks
- Mark tasks as done
- Delete tasks
- Save/load tasks in a text file
"""

import os

TODO_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    if line.startswith("[x] "):
                        tasks.append({"task": line[4:], "done": True})
                    else:
                        tasks.append({"task": line[4:] if line.startswith("[ ] ") else line, "done": False})
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for t in tasks:
            status = "[x]" if t["done"] else "[ ]"
            f.write(f"{status} {t['task']}\n")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\nYour tasks:")
    for idx, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✖"
        print(f"{idx}. [{status}] {t['task']}")

def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print(f"Task '{task}' added.")

def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[num-1]['task']}' marked as done.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            task = tasks.pop(num-1)
            save_tasks(tasks)
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    print("=== Simple To-Do List ===")
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Quit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-5.")

if __name__ == "__main__":
    main()