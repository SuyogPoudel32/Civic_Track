from flask import session,redirect,request
from modules.data_login_data import fetch_user_data
def loginUser(cursor):
    user_id = session.get("user_id")
    if user_id:
        return redirect("/dashboard")
    if request.method == "POST":
        input_data  = request.get_json()
        email = input_data["email"].strip()
        password = input_data["password"].strip()
        database_data = fetch_user_data(cursor,email,password)
        if database_data is None:
            return {"success": False}
        else:
            user_id = database_data[0][0]
            email = database_data[0][1]
            full_name = database_data[1][0]
            ward_no = database_data[1][1]
            session.clear()
            session["user_id"] = user_id
            session["full_name"] = full_name
            session["ward_no"] = ward_no
            return {"success": True,"user_name": full_name,"email": email,"ward_no": ward_no}