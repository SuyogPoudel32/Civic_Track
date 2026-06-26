from modules.save_register_data import Register
def fetch_verify_otp(cursor,email,otp,conn):
    cursor.execute("SELECT email,otp FROM pending_users WHERE email = %s",(email,))
    data = cursor.fetchone()
    if(otp == data[1]):
        cursor.execute("UPDATE pending_users SET is_verified = 1 WHERE email = %s",(email))
        conn.commit()
        obj = Register(cursor, email, conn)
        obj.save_users()
        return { "is_verified": True,
            "message": "OTP verified successfuly"
            
            }
    
    else:
        return  { "is_verified": False,
            "message": "OTP is incorrect"
            
            }
    

def set_data(cursor, data_dict, conn, email,phone_no):
    try:

        print(data_dict)

        cursor.execute(
            "SELECT * FROM pending_users WHERE email = %s",
            (email,)
        )

        response = cursor.fetchone()
        cursor.execute("SELECT * FROM pending_users WHERE phone_no = %s",(phone_no,))
        response_phone = cursor.fetchone()
        if response or response_phone:
            return {
                "success": False,
                "message": "Email or Phone already exists"
            }


        cursor.execute(" INSERT INTO pending_users (full_name, email, phone_no, password, ward_no, otp, role) VALUES (%s,%s,%s,%s,%s,%s,%s)",(
            data_dict["full_name"],
            email,
            data_dict["phone_no"],
            data_dict["password"],
            data_dict["ward_no"],
            data_dict["otp"],
            data_dict["role"]
        ))


        conn.commit()

        return {
            "success": True,
            "message": f"OTP sent successfully to {email}"
        }


    except Exception as e:
        conn.rollback()
        print(e)

        return {
            "success": False,
            "message": "Something went wrong"
        }