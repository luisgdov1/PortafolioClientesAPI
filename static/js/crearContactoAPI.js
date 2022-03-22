var formulario = document.getElementById("contactoForma")
var respuesta = document.getElementById("respuesta")
formulario.addEventListener('submit', function (e) {
    e.preventDefault();
    var nombre = document.getElementById("nameC").value
    var email = document.getElementById("emailC").value
    var telefono = document.getElementById("phoneC").value
    var mensaje= document.getElementById("messageC").value



    fetch('api/contacto/', {
        method: 'POST',
        body: JSON.stringify(
            {
        nombre_Contacto: nombre,
        telefono_Contacto: telefono,
        email_Contacto: email,
        mensaje_Contacto: mensaje
    }
        )
    })
        .then(res=> res.json())
        .then(data => {
            console.log(data)
            respuesta.innerHTML = ' <div class="alert alert-primary" role="alert">\n' +
                '                                Tus datos han sido enviados, espera una respuesta pronto\n' +
                '</div>'
        })
    formulario.reset()
})