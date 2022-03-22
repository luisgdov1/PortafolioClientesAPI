var formulario = document.getElementById("busqueda")
var contenedor = document.getElementById("resultados")
document.getElementById("cargarJson").addEventListener('click', displayJSON)
document.getElementById("descargarExcel").addEventListener('click', descargarExcel)

formulario.addEventListener('submit', function (e) {
    e.preventDefault();
    var criterio = document.getElementById("cuadro_busqueda").value

    var url = "api/busqueda/".concat(criterio).concat("/1")

    console.log(url)


    fetch(url)
        .then(response => response.json())
        .then(function (data) {}
            )
        ;


})

function displayJSON()
{
    var criterio = document.getElementById("cuadro_busqueda").value
    var url = "api/busqueda/".concat(criterio).concat("/1")
    fetch(url)
        .then(response => response.json())
        .then(function (data) {

            let html_final =""
            let nombre = "";
            let email ="";
            console.log(data["clientes"])
            //data['clientes'].forEach(function (data) {
            //    html += '<li>data["clientes"].nombre_Cliente - data.email_Cliente</li>'
            //})
            for (var i = 0; i<data['clientes'].length; i++)
            {
                nombre = data["clientes"][i]["nombre_Cliente"];
                email = data["clientes"][i].email_Cliente;
                console.log(nombre);
                //html = '<p>data["clientes"][i].nombre_Cliente - data["clientes"][i].email_Cliente</p>';
                contenedor.innerText += nombre + "\n"
            }
        })
}

function descargarExcel() {
    var criterio = document.getElementById("cuadro_busqueda").value
    var url = "api/busqueda/".concat(criterio).concat("/2")
    window.location.href = url
}