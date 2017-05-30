import os

command_history = list()

def main():
    username = raw_input("Username: ")
    sysname = "work"
    current_path = os.path.abspath(__file__)

    while True:
        command = raw_input(username+"@"+sysname+"$ ")
        command_history.append(command)
        ret = check_input(command)
        if ret is True:
            break;

    
def check_input(command):
    if command == "exit":
        return True;
    elif command == "ls":
        list_directory()
    elif command == "calc":
        calculator()
    elif command == "history":
        list_history()
    elif command == "":
        pass
    else:
        print 'command "'+command+'" not found'

def list_directory():
    for f in os.listdir(os.getcwd()):
        print f

def list_history():
    for c in command_history:
        print c

def calculator():
    result = eval(raw_input("Expression: "))
    print result

if __name__ == '__main__':
    main()
