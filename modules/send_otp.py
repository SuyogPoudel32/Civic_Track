from flask import session
from modules.encript_password import encription
from modules.otp_processing import set_data
def send_otp(cursor,full_name,phone_no,ward_no,otp,role,email,password,conn):
    cursor.execute("SELECT * FROM pending_users where email = %s",(email,))
    check_user_veified = cursor.fetchone()
    encripted_password = encription(password)
    if check_user_veified:
            if check_user_veified[8] == 0:
                cursor.execute("DELETE FROM pending_users where email = %s",(email))
                conn.commit()
        # send_otp_email(email,full_name,otp)
    pending_users = {
            "full_name": full_name,
            "phone_no": phone_no,
            "ward_no": ward_no,
            "password": encripted_password,
            "otp": str(otp),
            "role": role
    }
    response = set_data(cursor,pending_users,conn,email,phone_no)
    session["verify_email"] = email
    return response