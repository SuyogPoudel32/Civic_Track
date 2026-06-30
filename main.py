import pymysql
import random
from flask import Flask, render_template,request,redirect,jsonify,session
from modules.stats import get_reports
from modules.data_login_data import fetch_user_data
from modules.otp_processing import set_data
from modules.otp_processing import fetch_verify_otp
from modules.otp_sender import send_otp_email
from modules.encript_password import encription
import uuid
import os
from modules.save_report_data import UserReports
from werkzeug.utils import secure_filename


#import the modules
from modules.login import loginUser
from modules.send_otp import send_otp as otp_sender
from modules.login_required_decorator import login_required

app = Flask(__name__)
UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = ""

import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="civic_issue_reporting_system"
)
cursor = conn.cursor()
# query = """CREATE TABLE pending_users (
#     pending_id INT AUTO_INCREMENT PRIMARY KEY,
#     full_name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) NOT NULL UNIQUE,
#     phone_no VARCHAR(15) NOT NULL,
#     password VARCHAR(255) NOT NULL,
#     ward_no INT NOT NULL,
#     otp VARCHAR(6) NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     role VARCHAR(10)
# );
# """
# cursor.execute(query)


@app.route("/")
def home():
    all_reports = get_reports(cursor)
    return render_template("index.html",all_reports=all_reports)


@app.route("/login", methods=["GET", "POST"])
def login():
    response = loginUser(cursor) # Call the loginUser module from modules folder
    if response:
        return response
    return render_template("login.html")

@app.route("/register")
def register():
    # user_id = session.get("user_id")
    # if user_id:
    #     return redirect("/dashboard")
    return render_template("register.html")


@app.route("/otp-verification", methods=["GET","POST"])
def verify_otp():

    email = session.get("verify_email")

    if not email:
        return redirect("/register")

    if request.method == "POST":

        data = request.get_json()
        otp = data.get("verification_code")

        result = fetch_verify_otp(cursor, email, otp,conn)

        return result

    return render_template("verify.html")


@app.route("/send-otp",methods=["GET","POST"])
def send_otp(role = "user"):
    otp = random.randint(100000, 999999)
    if request.method == "POST":
        data = request.get_json()
        full_name = data["full_name"]
        email = data["email"]
        phone_no = data["phone_no"]
        password = data["password"]
        ward_no = data["ward_no"]
        response = otp_sender(cursor,full_name,phone_no,ward_no,otp,role,email,password,conn)
        if response:
            return response
    return render_template("verify.html")


from modules.get_categories_data import Reports
@app.route("/dashboard",methods=["GET","POST"])
@login_required
def dashboard():

    full_name = session.get("full_name")
    user_id = session.get("user_id")
    print(full_name,user_id)
    if request.method == "POST":
            report_obj = Reports(cursor)
            category_response = report_obj.get_categories_data()
            monthly_analytics_activity_response = report_obj.get_monthly_analytics_activity()
            print(category_response)
            if category_response:
                return {
                    "category_response": category_response,
                    "month_response": monthly_analytics_activity_response
                }
            else:
                return "Some Error occured"
        # return {
        #     "success": True
        # }
    return render_template("dashboard.html",full_name=full_name.capitalize())
    # return render_template("dashboard.html")

@app.route("/report_issue",methods=["GET","POST"])
def report_issue():
    file_urls = []
    user_id = session.get("user_id")
    ward_no = session.get("ward_no")
    upload_id = str(uuid.uuid4())
    if request.method=="POST":
        files = request.files.getlist("issue_images")
        issue_type = request.form.get("issue_type").strip()
        title = request.form.get("title").strip()
        location = request.form.get("location").strip()
        description = request.form.get("description").strip()
        option = request.form.get("issue_type").strip()
        # split the latitude and longitude
        parts = location.split(",")
        try:
            latitude = float(parts[0])
            longitude = float(parts[1])
        except (ValueError, IndexError):  # it shows that the location is string
            latitude = 0
            longitude = 0
            location_name = location

        report_data = {
            "user_id": user_id,
            "category_id": option,
            "ward_no": ward_no,
            "title": title,
            "description": description,
            "latitude": latitude,
            "longitude": longitude,
            "location_name": location_name
        }
        print(report_data)
        # user_reports_obj = UserReports(cursor,conn) #creates obj of UserReports
        # user_reports_obj.save_reports(report_data)
        # if files and issue_type and title and location and description:
        #     folder = os.path.join(
        #     app.config['UPLOAD_FOLDER'],str(user_id))
        #     if not os.path.exists(folder):
        #         print("Folder Created")
        #         os.mkdir(folder)
        #     issue_folder = os.path.join(folder,upload_id)
        #     os.makedirs(issue_folder)
        #     for file in files:
        #         filename = secure_filename(file.filename)
        #         file_url = os.path.join(issue_folder,filename)
        #         file.save(file_url)
        #         user_reports_obj.save_images(file_url)
            


        
        
        # filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # images = request.files.getlist("issue_images[]");
    return render_template("report_issue.html")
if __name__ == "__main__":
    app.run(debug=True)
