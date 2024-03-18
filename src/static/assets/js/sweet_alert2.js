function delete_alert(title, e) {

Swal.fire({
    title: title,
    showCancelButton: true,
    cancelButtonText: 'Cancelar',
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


function cancel_edition(title, redirect) {

Swal.fire({
    title: title,
    icon: "success",
    showConfirmButton: false,
    backdrop: true,
    showLoaderOnConfirm: true,
    timer: 1500,
    allowOutsideClick: false,
    allowEscapeKey: false,
})
setTimeout(function(){
            window.location.href = redirect;
         }, 1500);
};