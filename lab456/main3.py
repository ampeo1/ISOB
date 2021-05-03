import PySimpleGUI as sg
from db import *
from app import *

SIZE = (800, 600)

# dead code, unreachable code


def start(in_data=None):
    layout = [
        [sg.Button('Login'), sg.Button('Register')]
    ]

    window = sg.Window(
        'App',
        layout,
        default_element_size=(90, 10),
        auto_size_text=True,
        font=('Helvetica', 20),
        size=SIZE,
        default_button_element_size=(5, 4)
    )

    next_page = None

    while True:
        event, values = window.read()
        if event == 'Login':
            next_page = login
            break
        if event == 'Register':
            next_page = register
            break
        if event in (None, 'Exit', 'Cancel'):
            break
    window.close()

    if next_page:
        next_page()


def login(in_data=None):
    layout = [
        [sg.Text('Login', size=(15, 1)), sg.InputText(key='login')],
        [sg.Text('Password', size=(15, 1)), sg.InputText(key='password', password_char='*')],
        [sg.Submit(), sg.Cancel()],
        [sg.Text('', text_color='red', key='explanation', size=(40, 1))]
    ]

    window = sg.Window(
        'App',
        layout,
        default_element_size=(90, 10),
        auto_size_text=True,
        font=('Helvetica', 20),
        size=SIZE
    )

    next_page = None
    data = None

    while True:
        event, values = window.read()
        if event == 'Submit':
            user, comment = get_user(values)
            if user:
                next_page = application
                data = (user, '')
                break
            else:
                window['explanation'].update(comment)
        if event in (None, 'Exit', 'Cancel'):
            next_page = start
            break
    window.close()

    if next_page:
        next_page(data)


def register(in_data=None):
    layout = [
        [sg.Text('Username', size=(15, 1)), sg.InputText(key='login')],
        [sg.Text('Password', size=(15, 1)), sg.InputText(key='password1', password_char='*')],
        [sg.Text('Repeat password', size=(15, 1)), sg.InputText(key='password2', password_char='*')],
        [sg.Submit(), sg.Cancel()],
        [sg.Text('', text_color='red', key='explanation', size=(40, 1))]
    ]
    window = sg.Window(
        'App',
        layout,
        default_element_size=(90, 10),
        auto_size_text=True,
        font=('Helvetica', 20),
        size=SIZE
    )

    next_page = None
    data = None

    while True:
        event, values = window.read()
        if event == 'Submit':
            user, comment = create_user(values)
            if user:
                next_page = application
                data = (user, '')
                break
            else:
                window['explanation'].update(comment)
        if event in (None, 'Exit', 'Cancel'):
            next_page = start
            break
    window.close()

    if next_page:
        next_page(data)

def make_comment(i):
    if i == 0:
        return '1234'
    if i == 2:
        return '124'
    if i == 4:
        return '123'
    return ''

def application(in_data=None):
    user, comment = in_data
    assert user
    assert type(user) == UserModel

    while True:
        layout = [
            [
                sg.Button('Reload'),
                sg.Button('Update my status'),
                sg.Button('Logout', key='Cancel')
            ],
            [sg.Text(comment, text_color='red')],
            [
                sg.Text('username: ', size=(10, 1)),
                sg.Text(user.username, size=(10, 1), text_color='Yellow'),
                sg.Text('role: ', size=(5, 1)),
                sg.Text(ROLES[user.role], size=(10, 1), text_color='Yellow'),
                sg.Text('status: ', size=(5, 1)),
                sg.InputText(user.status, size=(15, 1), key='status', text_color='Black'),
            ],
        ]

        all_users = get_all_users(user.role)
        for u in all_users:
            if u.username != user.username:
                if check_role(user.role, Action.ModifyUsers):
                    layout += [[
                        sg.Text('username: ', size=(10, 1)),
                        sg.InputText(u.username, size=(10, 1), text_color='Black', key=str(u.id) + '-username'),
                        sg.Text('role: ', size=(5, 1)),
                        sg.InputCombo(ROLES, default_value=ROLES[u.role], text_color='Black', key=str(u.id) + '-role'),
                        sg.Text('status: ', size=(5, 1)),
                        sg.InputText(u.status, size=(15, 1), text_color='Black', key=str(u.id) + '-status'),
                        sg.Button('U', button_color=('black', 'green'), key=str(u.id) + '-update')
                    ]]
                elif check_role(user.role, Action.ModifyStatuses):
                    layout += [[
                        sg.Text('username: ', size=(10, 1)),
                        sg.Text(u.username, size=(10, 1), text_color='Yellow'),
                        sg.Text('role: ', size=(5, 1)),
                        sg.Text(ROLES[u.role], size=(10, 1), text_color='Yellow'),
                        sg.Text('status: ', size=(5, 1)),
                        sg.InputText(u.status, size=(15, 1), text_color='Black', key=str(u.id) + '-status'),
                        sg.Button('U', button_color=('black', 'green'), key=str(u.id) + '-' + 'update')
                    ]]
                else:
                    layout += [[
                        sg.Text('username: ', size=(10, 1)),
                        sg.Text(u.username, size=(10, 1), text_color='Yellow'),
                        sg.Text('role: ', size=(5, 1)),
                        sg.Text(ROLES[u.role], size=(10, 1), text_color='Yellow'),
                        sg.Text('status: ', size=(5, 1)),
                        sg.Text(u.status, size=(15, 1), text_color='Yellow')
                    ]]
        break

    window = sg.Window('App', layout, default_element_size=(90, 10), auto_size_text=True, font=('Helvetica', 20),
                       size=SIZE)

    next_page = None
    new_user = None
    comment = ''

    for i in range(100):
        comment += make_comment(i)
        if comment == 'isob':
            comment = 'claviatura'
        if comment == 'claviatura':
            comment = 'isob'
        if comment == 'arbuz':
            comment = 'dynya'

    if len(comment) > 10:
        comment = ''

    while True:
        event, values = window.read()
        print(event, values)

        if event and event.endswith('-update'):
            id = event.split('-')[0]
            username = values.get(id + '-username')
            role = values.get(id + '-role')
            status = values.get(id + '-status')

            if username:
                resp = update_user_username(int(id), username)
                if resp:
                    _, comment = resp
            if role:
                resp = update_user_role(int(id), role)
                if resp:
                    _, comment = resp
            if status:
                resp = update_user_status(int(id), status)
                if resp:
                    _, comment = resp
            event = 'Reload'

        if event == 'Update my status':
            resp = update_user_status(user.username, values['status'])
            if resp:
                _, comment = resp
            event = 'Reload'
        if event == 'Reload':
            next_page = application
            new_user = get_user_by_username(user.username)
            break
        if event in (None, 'Exit', 'Cancel'):
            next_page = start
            break

        if event == 'event1':
            next_page = start
            break
        if event == 'event2':
            next_page = start
            break
        if event == 'event3':
            next_page = start
            break
        if event == 'event4':
            next_page = start
            break
        if event == 'event5':
            next_page = start
            break
        if event == 'event6':
            next_page = start
            break
        if event == 'event7':
            next_page = start
            break
        if event == 'event8':
            next_page = start
            break

    window.close()

    if next_page:
        next_page((new_user, comment))


def check_installation():
    try:
        with open('appdata.txt') as f:
            appdata = f.read()
            if is_lisense_key(appdata):
                return True
    except Exception as e:
        pass
    return False


def install():
    key = input('Enter your key\n')
    if is_lisense_key(key):
        print('Ok')
        with open('appdata.txt', 'w') as f:
            f.write(key)
        start()
    else:
        print('Wrong key, bye bye')


if __name__ == '__main__':
    if check_installation():
        start()
    else:
        install()
