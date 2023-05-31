def get_todos(filepath='todos.txt'):
    """Read txt file and return list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """Write the to-do items in the txt file"""
    with open('todos.txt', 'w') as file:
        file.writelines(todos_arg)

