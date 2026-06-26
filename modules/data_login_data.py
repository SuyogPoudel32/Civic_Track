from modules.encript_password import check_password
def fetch_user_data(cursor,email,password):
    cursor.execute("SELECT user_id,email,password from credentials WHERE email = %s", (email,))
    credentials_data = cursor.fetchone()
    if credentials_data:
        response = check_password(password,credentials_data[2])
        if response == "success":
            cursor.execute("SELECT full_name , ward_no from users where user_id = %s",(credentials_data[0]))
            user_data = cursor.fetchone()
            return credentials_data,user_data
        else:
            return None