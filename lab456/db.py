import sqlite3
from app import *
from hashlib import md5 as md5
from time import time, sleep

conn = sqlite3.connect('file:my.db?mode=rw', uri=True)
print('loaded db')


class UserModel:
    def __init__(self, data_tuple):
        self.id = data_tuple[0]
        self.username = data_tuple[1]
        self.password_hash = data_tuple[2]
        self.role = data_tuple[3]
        self.status = data_tuple[4]

conn.execute("""CREATE TABLE IF NOT EXISTS user(
   id INT PRIMARY KEY,
   username TEXT,
   password_hash TEXT,
   role INT,
   status TEXT);
""")
conn.commit()
MAX_LENGTH = 20


def anti_buffer_overflow(query):
    def wrapper(*args):
        check_failed = False
        explanation = ''
        for a in args:
            if type(a) == str:
                if len(a) > MAX_LENGTH:
                    check_failed = True
                    explanation = 'Argument is too long (maxlength=20)'
            elif type(a) == dict:
                for k, v in a.items():
                    if type(v) == str and len(v) > MAX_LENGTH:
                        check_failed = True
                        explanation = 'Argument {} is too long (maxlength=20)'.format(str(k))
        if check_failed:
            print(explanation)
            return None, explanation
        return query(*args)
    return wrapper


class LastRequest(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LastRequest, cls).__new__(cls)
            cls.last_call = time()
        return cls.instance


def anti_dudos(query):
    def wrapper(*args):
        now = time()
        time_to_sleep = LastRequest().last_call + 0.2 - now
        LastRequest().last_call = now
        if time_to_sleep > 0:
            sleep(time_to_sleep)
        return query(*args)
    return wrapper


@anti_buffer_overflow
@anti_dudos
def get_user(logpass):
    password_hash = md5(logpass['password'].encode()).hexdigest()
    cursor = conn.cursor()

    cursor.execute(
        '''
            SELECT * from user
            WHERE username=? and password_hash=?;
        ''', [(logpass['login']), (password_hash)]
    )

    # sql = '''
    #         SELECT * from user
    #         WHERE username='{}' and password_hash='{}';
    #     '''.format(logpass['login'], password_hash)
    # # kek' or role=2; --
    # cursor.execute(
    #     sql
    # )

    user = cursor.fetchone()
    conn.commit()
    if not user:
        return None, 'Login or password incorrect'
    return UserModel(user), ''


@anti_dudos
def get_user_by_username(username):
    cursor = conn.cursor()

    cursor.execute(
        '''
            SELECT id, username, '', role, status  from user 
            WHERE username=?;
        ''', [(username)]
    )

    user = cursor.fetchone()
    conn.commit()
    if not user:
        return None
    return UserModel(user)


@anti_dudos
def get_all_users(role):
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT id, username, '', role, status from user;
        '''
    )

    users = list(map(UserModel, cursor.fetchall()))
    conn.commit()

    return users


@anti_buffer_overflow
@anti_dudos
def update_user_username(id, username):
    cursor = conn.cursor()

    cursor.execute(
        '''
            UPDATE user SET username=?  
            WHERE id=?;
        ''', [(username), (id)]
    )

    conn.commit()
    return None


@anti_buffer_overflow
@anti_dudos
def update_user_role(id, role):
    cursor = conn.cursor()

    role = Role.parse(role)

    cursor.execute(
        '''
            UPDATE user SET role=?  
            WHERE id=?;
        ''', [(role), (id)]
    )

    conn.commit()
    return None


@anti_buffer_overflow
@anti_dudos
def update_user_status(username, status):
    cursor = conn.cursor()

    if type(username) == int:
        cursor.execute(
            '''
                UPDATE user SET status=?  
                WHERE id=?;
            ''', [(status), (username)]
        )
    else:
        # update my status
        cursor.execute(
            '''
                UPDATE user SET status=?  
                WHERE username=?;
            ''', [(status), (username)]
        )
    conn.commit()
    return None


@anti_buffer_overflow
@anti_dudos
def create_user(logpass):
    if not logpass['password1'] or logpass['password1'] != logpass['password2']:
        return None, 'Passwords mismatch or password is empty'
    password_hash1 = md5(logpass['password1'].encode()).hexdigest()
    cursor = conn.cursor()
    print(logpass)
    try:
        cursor.execute(
            '''
            INSERT INTO user 
            VALUES 
            (NULL, ?, ?, 0, '');
            ''',
            [(logpass['login']), (password_hash1)])
        logpass['password'] = logpass['password1']
        conn.commit()
        return get_user(logpass)  # returns pair
    except Exception as e:
        print(e)
        return None, 'This user already exists'

