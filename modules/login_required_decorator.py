from flask import session,redirect
def login_required(func):
    def wrapper(*args,**kwargs):
        user_id = session.get("user_id")
        if not user_id:
            return redirect("/login")
        print("logged")
        return func(*args,**kwargs)
    return wrapper
