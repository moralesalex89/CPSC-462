from User import User


def createUser(userType, username, password):
    return 1


def authenticate(username, password):
    if username == "Guest":
        return User(0, "Guest","TestG")

    if username == "Employee":
        return User(1, "Employee", "TestE")

    else:
        return User(0, "", "")

