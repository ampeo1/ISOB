ROLES = [
    'User',
    'Moderator',
    'Admin',
]


class Role:
    User = 0
    Moderator = 1
    Admin = 2

    @staticmethod
    def parse(role):
        for i in range(len(ROLES)):
            if ROLES[i] == role:
                return i
        raise


class Action:
    ModifyUsers = Role.Admin
    ModifyStatuses = Role.Moderator


def check_role(role, action):
    return role >= action


MOD = 10 ** 29 + 123456789
EXP = 422912957897648718792123824


def rem(key):
    return pow(int(key, 16), EXP, MOD)


def is_lisense_key(key):
    if type(key) != str:
        return False
    try:
        return rem(key) == 8107257653004806299847340918
    except:
        return False


def get_new_key():
    key = input()
    return rem(key)

