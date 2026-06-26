import smtplib
from email.message import EmailMessage

def send_otp_email(receiver_email, full_name, otp):

    msg = EmailMessage()

    msg["Subject"] = "Verify Your Email Address"
    msg["From"] = "monserratshauntae765@gmail.com"
    msg["To"] = receiver_email

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body style="margin:0;padding:0;background-color:#f4f4f4;font-family:Arial,sans-serif;">

        <div style="max-width:600px;margin:30px auto;background:#ffffff;border-radius:10px;overflow:hidden;box-shadow:0 0 10px rgba(0,0,0,0.1);">

            <div style="background:#2563eb;padding:20px;text-align:center;">
                <h1 style="color:white;margin:0;">
                    Civic Issue Reporting System
                </h1>
            </div>

            <div style="padding:30px;">

                <h2 style="color:#333;">
                    Hello {full_name},
                </h2>

                <p style="font-size:16px;color:#555;">
                    Thank you for registering. Please use the verification code below to verify your email address.
                </p>

                <div style="
                    text-align:center;
                    margin:30px 0;
                    padding:20px;
                    background:#eff6ff;
                    border:2px dashed #2563eb;
                    border-radius:8px;
                ">
                    <span style="
                        font-size:36px;
                        font-weight:bold;
                        letter-spacing:8px;
                        color:#2563eb;
                    ">
                        {otp}
                    </span>
                </div>

                <p style="font-size:15px;color:#555;">
                    ⏰ This OTP is valid for <strong>5 minutes</strong>.
                </p>

                <p style="font-size:15px;color:#555;">
                    🔒 Do not share this code with anyone.
                </p>

                <p style="font-size:15px;color:#555;">
                    If you did not request this verification, you can safely ignore this email.
                </p>

            </div>

            <div style="
                background:#f8fafc;
                padding:15px;
                text-align:center;
                color:#666;
                font-size:12px;
            ">
                © 2026 Civic Issue Reporting System<br>
                Automated Verification Email
            </div>

        </div>

    </body>
    </html>
    """

    msg.set_content(
        f"""
Hello {full_name},

Your OTP is: {otp}

Do not share this code with anyone.

Civic Issue Reporting System
"""
    )

    msg.add_alternative(html_content, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            "monserratshauntae765@gmail.com",
            "jxus sebq lwqd sxvo"
        )
        server.send_message(msg)