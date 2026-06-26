export function error_message_throw(title, icon = "error") {
                Swal.fire({
                toast: true,
                position: "top-end",
                icon: icon,
                title: title,
                showConfirmButton: false,
                timer: 3000,
            });
    }
