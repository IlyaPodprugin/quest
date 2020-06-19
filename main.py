import functions
import messages


def check_user_command():
    user_command = input()
    if user_command == 'reg':
        functions.registration()
    elif user_command == 'auth':
        functions.authorisation()
    check_user_command()


print(messages.hello)
check_user_command()
