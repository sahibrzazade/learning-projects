no_tasks_message = "The to-do list is empty. Please add tasks first."
to_do_items = []

def add_item(name):
    task = {
        "name": name,
        "is_done": False
    }
    to_do_items.append(task)
    print(f'Task "{name}" added to the to-do list.')

def view_items():
    if not to_do_items:
        print(no_tasks_message)
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(to_do_items, start=1):
            status = "✅ Done" if task["is_done"] else "❌ Not Done"
            print(f"{index}. {task['name']} - {status}")

def remove_item(index):
    if 0 <= index < len(to_do_items):
        removed_item = to_do_items.pop(index)
        print(f'Task "{removed_item["name"]}" removed from the to-do list.')
    else:
        print("Invalid index. Please try again.")

def rename_item(index, new_name):
    if 0 <= index < len(to_do_items):
        old_name = to_do_items[index]["name"]
        to_do_items[index]["name"] = new_name
        print(f'Task "{old_name}" renamed to "{new_name}".')
    else:
        print("Invalid index. Please try again.")

def toggle_task_status(index):
    if 0 <= index < len(to_do_items):
        task = to_do_items[index]
        task["is_done"] = not task["is_done"]
        status = "Done" if task["is_done"] else "Not Done"
        print(f'Task "{task["name"]}" status toggled to {status}.')
    else:
        print("Invalid index. Please try again.")

def is_item_exist():
    return len(to_do_items) > 0

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Rename Task")
        print("4. Toggle Task Status")
        print("5. Remove Task")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            name = input("Enter the task name: ")
            add_item(name)

        elif choice == '2':
            view_items()

        elif choice == '3':
            if not is_item_exist():
                print(no_tasks_message)
                continue
            try:
                if(len(to_do_items) == 1):
                    index = 0
                else:
                    index = int(input(f"Enter a task number between 1 and {len(to_do_items)} to rename: ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            new_name = input("Enter the new task name: ")
            rename_item(index, new_name)

        elif choice == '4':
            if not is_item_exist():
                print(no_tasks_message)
                continue
            try:
                if(len(to_do_items) == 1):
                    index = 0
                else:
                    index = int(input(f"Enter a task number between 1 and {len(to_do_items)} to toggle status: ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            toggle_task_status(index)

        elif choice == '5':
            if not is_item_exist():
                print(no_tasks_message)
                continue
            try:
                if(len(to_do_items) == 1):
                    index = 0
                else:
                    index = int(input(f"Enter a task number between 1 and {len(to_do_items)} to remove: ")) - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            remove_item(index)

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()