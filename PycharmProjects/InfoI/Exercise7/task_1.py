class Password:
    def __init__(self, name, username, password):
        self._name = name
        self._username = username
        self._password = password

    def pretty_str_password():
        return "%s: %s /%s" %(self._name, self._username, self._password)

def __str__():
    return "%s: %s/" %(Password._name,Password._username)+ len(Password._password)*"*"

class PasswordManager:
    def __init__(self, master_password):
        self._master_password = master_password
        self._passwords = {}
        self.unlocked = False

def lock():
    PasswordManager.unlocked = False

def unlock(master_password):
    if master_password == PasswordManager._master_password:
        PasswordManager.unlocked = True
        return PasswordManager.unlocked

def create_new_password(name, username, password):
    if PasswordManager.unlocked == True:
        if name not in PasswordManager._passwords:
            PasswordManager._passwords[username]== password
            return password
        else:
            return None
    else:
        return None

def update_password(name, username, password):
    if PasswordManager.unlocked == True:
        for key in PasswordManager._passwords.keys():
            if key == name:
                PasswordManager._passwords[key]=password
                PasswordManager._passwords[username]=PasswordManager._passwords.pop(name)
            return password
        else:
            return None
    else:
        return None

def get_password(name):
    if PasswordManager.unlocked == True:
        for key in PasswordManager._passwords.keys():
            if PasswordManager._passwords[name] == name:
                return PasswordManager._passwords[name]
            else:
                return None
    else:
        return None

def list_passwords():
    list = []
    if PasswordManager.unlocked == True:
        for key in PasswordManager._passwords.keys():
            list.append(Password.pretty_str_password(PasswordManager._passwords[key]))
            return list
    else:
        for key in PasswordManager._passwords.keys():
            list.append(__str__(PasswordManager._passwords[key]))
            return list











