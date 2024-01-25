const delete_alert = (title, text) => {

    Swal.fire({
        titleText: title,
        text: text,
        icon: "warning",
        confirmButtonText: "Si"
    });
};
