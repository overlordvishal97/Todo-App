import PySimpleGUI as sg
import functions

FILEPATH = "todos_item.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and returns the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """write the to-do items in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

layout = [
    [sg.Text("Type in a to-do"), sg.InputText(key='todo', tooltip="Enter todo")],
    [sg.Button("Add", key='add')],
]

window = sg.Window('My Todo App', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'add':
        todo = values['todo']
        if todo.strip():  # Check if the input is not empty
            todos = get_todos()
            todos.append(todo + '\n')
            write_todos(todos)
            sg.popup(f'To-do "{todo}" added successfully!')

window.close()
