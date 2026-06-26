class resistration {
    constructor() {
        this.form = document.getElementById("form");
        this.full_name = document.getElementById("full_name");
        this.verify_form = document.getElementById("verify_form");
        this.email = document.getElementById("email");
        this.phone_no = document.getElementById("phone_no");
        this.register_password = document.getElementById("register_password");
        this.confirm_password = document.getElementById("confirm_password");
        this.ward_no = document.getElementById("ward_no")
        if (this.form) {
            this.form.addEventListener("submit", (e) => {
                e.preventDefault();
                this.register();
            });
        }


        if (this.verify_form) {
            this.verify_form.addEventListener("submit", (e) => {
                e.preventDefault();

                const otp = document.getElementById("verification_code").value;

                this.verify_otp(otp);
            });
        }
    }
    error_message_throw(title, icon = "error") {
        if (title == "Invalid Password") {
            Swal.fire({
                icon: icon,
                title: "Invalid Password",
                html: `
            Password must contain:
            <br>• At least 8 characters
            <br>• One uppercase letter (A-Z)
            <br>• One lowercase letter (a-z)
            <br>• One number (0-9)
            <br>• One special character (@$!%*?&)
        `
            });
        }
        else {
            Swal.fire({
                toast: true,
                position: "top-end",
                icon: icon,
                title: title,
                showConfirmButton: false,
                timer: 3000,
            });
        }
        return
    }

    register() {
        const full_name = this.full_name.value.trim()
        const phone_no = this.phone_no.value.trim()
        const email = this.email.value.trim()
        const ward_no = this.ward_no.value.trim()
        const register_password = this.register_password.value.trim()
        const confirm_password = this.confirm_password.value.trim();


        const cols = [
            full_name,
            phone_no,
            email,
            ward_no,
            register_password

        ];
        const regexes = [
            /^[A-Za-z\s]{2,50}$/,
            /^(98|97|96)\d{8}$/,
            /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
            /^(?:[1-9]|1[0-5])$/,
            /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/
        ]
        const errors = [
            "Invalid Full Name",
            "Invalid Phone Number",
            "Invalid Email",
            "Invalid Ward Number",
            "Invalid Password",
        ]
        for (let i = 0; i < cols.length; i++) {
            if (!cols[i]) {
                this.error_message_throw("Please fill all fields");
                return;
            }

            if (!regexes[i].test(cols[i])) {
                this.error_message_throw(errors[i]);
                return;
            }
        }
        if (register_password != confirm_password) {
            this.error_message_throw("Password and confirm password doesn't match");
            return
        }
        else {
            console.log("Good");
            this.otp(full_name, email, phone_no, register_password, ward_no);
        }
    }

    async otp(full_name, email, phone_no, password, ward_no) {
        const btn = document.getElementById("create_account_btn");

        btn.disabled = true;
        btn.innerHTML = "Sending OTP...";

        const response = await fetch("/send-otp", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                full_name,
                email,
                phone_no,
                password,
                ward_no
            })
        })
        const data = await response.json();
        if (data["success"]) {
            this.error_message_throw(data["message"], "success")
            setTimeout(() => {
                window.location.href = "/otp-verification";

            }, 1000);
        }
        else {
            this.error_message_throw(data["message"])
            setTimeout(() => {
                window.location.href = "/login";

            }, 1000);

        }
    }
    async verify_otp(otp) {

        const response = await fetch("/otp-verification", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                verification_code: otp
            })
        });

        const data = await response.json();
        if (data.is_verified) {
            this.error_message_throw(data.message, "success");
        }
        else {
            this.error_message_throw(data.message);
        }
    }


}

obj = new resistration();





