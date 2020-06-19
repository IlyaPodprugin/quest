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
        print(messages.successful_registration)
        return
    print(messages.wrong_password)
    registration()
    return


def authorisation():
    global login
    global password
    # print(login, password)
    if login == input('Введите логин: '):
        if password == input('Введите пароль: '):
            print(messages.successful_authorisation)
            return
        print(messages.wrong_password)
        authorisation()
        return
    print(messages.wrong_login)
    authorisation()
    return


# def random_password_generator():
    # some code