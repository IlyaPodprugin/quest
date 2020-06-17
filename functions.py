import messages
login = ''
password = ''


def registration():
    global login
    global password
    login = input('Придумайте логин: ')
    password = input('Придумайте пароль: ')
    # print(login, password)
    if input('Подтвердите пароль: ') == password:
        return messages.successful_registration
    print(messages.wrong_password)
    return registration()


def authorisation():
    global login
    global password
    # print(login, password)
    if login == input('Введите логин: '):
        if password == input('Введите пароль: '):
            return messages.successful_authorisation
        print(messages.wrong_password)
        return authorisation()
    print(messages.wrong_login)
    return authorisation()


# def micro_game():
    