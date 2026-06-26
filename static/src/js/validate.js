class Login {
    constructor() {

        this.form = document.getElementById("form");
        this.emailInput = document.getElementById("email");
        // this.checkbox = document.getElementById("checkbox");

        this.passwordInput = document.getElementById("password");


        this.user_credentials = {}

        this.form.addEventListener("submit", (e) => {
            e.preventDefault();
            this.validate();
        });
    }

    async validate() {
        const email = this.emailInput.value;
        const password = this.passwordInput.value;


        const response = await fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email,
                password
            })
        });

        const data = await response.json();
        this.user_credentials = {
            email: data.email,
            password: data.password
        }


        if (data.success) {
            Swal.fire({
                toast: true,
                position: "top-end",
                icon: "success",
                title: "Verified",
                showConfirmButton: false,
                timer: 3000
            });
            setTimeout(() => {
                window.location.href = "/dashboard";
                
            }, 1000);
            // if (this.checkbox.checked) {
            //     this.checkbox.checked = false;
            // }

        } else {
            Swal.fire({
                toast: true,
                position: "top-end",
                icon: "error",
                title: "Wrong Credentials",
                showConfirmButton: false,
                timer: 3000
            });
        }

    }

}

console.log("Creating Login object");
window.loginObj = new Login();
console.log("Login object created");
