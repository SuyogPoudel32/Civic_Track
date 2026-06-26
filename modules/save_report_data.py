class UserReports:
    def __init__(self,cursor,conn):
        self.cursor = cursor
        self.conn = conn
        self.complaint_id = 0
    def save_reports(self,data):
        self.cursor.execute("""INSERT INTO complaints (user_id,category_id,ward_no,title,description,latitude,longitude)
                        VALUES(%s,%s,%s,%s,%s,%s,%s)     
                    
                    """,(data["user_id"],data["category_id"],data["ward_no"],
                            data["title"],data["description"],data["latitude"],data["longitude"]))
        self.conn.commit()
        self.complaint_id = self.cursor.lastrowid
        print("Save Successfully")

    
    def save_images(self,file_url):
        self.cursor.execute("""
        INSERT INTO complaint_images(complaint_id,image_url)
        VALUES(%s,%s)
        """,(self.complaint_id,file_url))
        self.conn.commit()
        print("Save images Successfully")