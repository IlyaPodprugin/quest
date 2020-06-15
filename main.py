import functions
from functions import login, password
import messages


def check_user_command():
    user_command = input()
    if user_command == 'reg':
        print(functions.registration())
    elif user_command == 'auth':
        print(functions.authorisation())
    check_user_command()

print(messages.hello_message)
check_user_command()