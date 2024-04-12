# Todo-App
This is a simple to-do list application implemented in both a command-line interface (CLI) and a graphical user interface (GUI) using Python. The application allows users to add, view, edit, and complete to-do items.

# Files
cli.py: Contains the command-line interface implementation of the to-do app.
gui.py: Contains the graphical user interface implementation of the to-do app using PySimpleGUI.
functions.py: Contains functions for reading and writing to-do items to a text file.
todos_item.txt: Text file to store the to-do items.

# How to Run
Command-line Interface (CLI)
Open a terminal or command prompt.
Navigate to the directory containing cli.py.
Run the command: python cli.py.
Follow the prompts to interact with the CLI to-do app.
Graphical User Interface (GUI)
Ensure you have PySimpleGUI installed. If not, you can install it via pip: pip install PySimpleGUI.
Open a terminal or command prompt.
Navigate to the directory containing gui.py.
Run the command: python gui.py.
The GUI window will appear. Follow the on-screen instructions to interact with the GUI to-do app.

# Functionality
Add: Allows users to add new to-do items.
Show: Displays the current list of to-do items.
Edit: Enables users to edit existing to-do items.
Complete: Marks a to-do item as completed and removes it from the list.
Exit: Terminates the program.

# Additional Notes
Both the CLI and GUI interfaces share the same backend functionality provided by functions.py.
To-do items are stored in a text file (todos_item.txt) using a simple text-based format.
