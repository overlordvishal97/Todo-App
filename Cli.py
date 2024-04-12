import functions
import time

def print_timestamp():
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print("It is", now)

def add_todo(todo):
    todos = functions.get_todos()
    todos.append(todo + '\n')
    functions.write_todos(todos)

def show_todos():
    todos = functions.get_todos()
    for index, item in enumerate(todos):
        item = item.strip('\n')
        row = f"{index + 1}-{item}"
        print(row)

def edit_todo():
    try:
        number = int(input("Enter the index of the todo you want to edit: "))
        todos = functions.get_todos()
        print('Here are the existing todos:', todos)
        new_todo = input("Enter the new todo: ")
        todos[number - 1] = new_todo + '\n'
        functions.write_todos(todos)
        print('Todo edited successfully.')
    except (ValueError, IndexError):
        print("Invalid index. Please enter a valid index.")

def complete_todo():
    try:
        number = int(input("Enter the index of the todo you want to complete: "))
        todos = functions.get_todos()
        if 1 <= number <= len(todos):
            removed_todo = todos.pop(number - 1).strip('\n')
            functions.write_todos(todos)
            print(f"Todo '{removed_todo}' completed successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid index. Please enter a valid index.")

print_timestamp()

while True:
    action = input("Type 'add', 'show', 'edit', 'complete', or 'exit': ").strip().lower()

    if action == 'add':
        todo = input("Enter the new todo: ")
        add_todo(todo)

    elif action == 'show':
        show_todos()

    elif action == 'edit':
        edit_todo()

    elif action == 'complete':
        complete_todo()

    elif action == 'exit':
        print('Goodbye!')
        break

    else:
        print("Command not recognized. Please try again.")
