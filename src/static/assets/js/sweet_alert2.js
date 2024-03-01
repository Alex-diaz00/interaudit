function delete_alert(title, e) {

Swal.fire({
    title: title,
    showCancelButton: true,
    icon: "warning",
    confirmButtonText: "Eliminar",
    confirmButtonColor: "#d33",
    backdrop: true,
    showLoaderOnConfirm: true,
    preConfirm:()=> {
        location.href = e.target.href;
                        },
    allowOutsideClick: false,
    allowEscapeKey: false,
})

};