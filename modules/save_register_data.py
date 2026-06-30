class Register:
    def __init__(self, cursor, email, conn):
        self.cursor = cursor
        self.conn = conn

        self.cursor.execute(
            "SELECT ward_no,full_name,role,phone_no,email,password FROM pending_users WHERE email = %s",
            (email,)
        )

        self.data = self.cursor.fetchone()
        print(self.data)
        self.ward_no = self.data[0]
        self.full_name = self.data[1]
        self.role = self.data[2]
        self.phone_no = self.data[3]
        self.email = self.data[4]
        self.password = self.data[5]


    def save_users(self):

        try:
            self.cursor.execute(" INSERT INTO users (full_name, role, ward_no, phone_no) VALUES (%s,%s,%s,%s)",(
                self.full_name,
                self.role,
                self.ward_no,
                self.phone_no
            ))

            self.user_id = self.cursor.lastrowid

            self.conn.commit()
            print("user saved")
            self.save_credentials()
            return True

        except Exception as e:
            print(e)
            self.conn.rollback()
            return False



    def save_credentials(self):

        try:
            self.cursor.execute(" INSERT INTO credentials (user_id,email,password) VALUES (%s,%s,%s)",(
                self.user_id,
                self.email,
                self.password
            ))
            print("Credentials saved")
            self.conn.commit()

            return True

        except Exception as e:
            print(e)
            self.conn.rollback()
            return False