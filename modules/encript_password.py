import bcrypt

def encription(password):
    hashed_password = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
    )
    return hashed_password

def check_password(enter_password,real_password):
    if bcrypt.checkpw(
        enter_password.encode(),
        real_password.encode()
    ):
        return "success"
    else:
        return "Invalid password"