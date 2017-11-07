todos = []

def addTodo(todo):
    todos.append(todo)

def removeTodo(todo):
    todos.remove(todo)

def listTodos(todo):
    print(todos)

while True:
    command = input('What do you wanna do? ')
    if command == 'add':
        todo = input('What to add? ')
        addTodo(todo)
    elif command == 'remove':
        todo = input('What to remove? ')
        removeTodo(todo)
    elif command == 'list':
        listTodos()
    elif command == 'exit':
        break
    else:
        print('Unknown Command')
