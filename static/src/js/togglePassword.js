function togglePassword(passwordId, eye) {
    const passwordInput = document.getElementById(passwordId);

    if (passwordInput.type === "password") {
        passwordInput.type = "text";

        eye.classList.remove("fa-eye");
        eye.classList.add("fa-eye-slash");
    } else {
        passwordInput.type = "password";

        eye.classList.remove("fa-eye-slash");
        eye.classList.add("fa-eye");
    }

    
}