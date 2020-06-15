import messages
login = ''
password = ''


def registration():
    global login
    global password
    login = input('Придумайте логин: ')
    password = input('Придумайте пароль: ')
    print(login, password)
    if input('Подтвердите пароль: ') == password:
        return messages.successful_registration_message
    return messages.registration_error_message


def authorisation():
    global login
    global password
    print(login, password)
    if login == input('Введите логин: '):
        if password == input('Введите пароль: '):
            return messages.successful_authorisation_message
        return 'Неверный пароль'
    return 'Неверный логин'