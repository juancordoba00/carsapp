function vehiculo_Eliminar(ruta){
    if(confirm('Está seguro?')){
        location.href = ruta;
    }
}

function vehiculo_Enviar(ruta){
    if(confirm('Está seguro que desea enviar el vehículo a revisión?')){
        location.href = ruta;
    }
}

function vehiculo_EnviarM(ruta){
    if(confirm('Está seguro que desea enviar el vehículo a mantenimiento?')){
        location.href = ruta;
    }
}

function asignarEmpleado(ruta){
    if(confirm('Está seguro que desea asignarse como empleado a cargo de este vehiculo?')){
        location.href = ruta;
    }
}

function App() {}

window.onload = function (event) {
    var app = new App();
    window.app = app;
};

App.prototype.processingButton = function(event) {
    const btn = event.currentTarget;
    const slickList = event.currentTarget.parentNode;
    const track = event.currentTarget.parentNode.querySelector('#track');
    const slick = track.querySelectorAll('.slick');

    const slickWidth = slick[0].offsetWidth;
    
    const trackWidth = track.offsetWidth;
    const listWidth = slickList.offsetWidth;

    track.style.left == ""  ? leftPosition = track.style.left = 0 : leftPosition = parseFloat(track.style.left.slice(0, -2) * -1);

    btn.dataset.button == "button-prev" ? prevAction(leftPosition,slickWidth,track) : nextAction(leftPosition,trackWidth,listWidth,slickWidth,track)
}

let prevAction = (leftPosition,slickWidth,track) => {
    if(leftPosition > 0) {
        console.log("entro 2")
        track.style.left = `${-1 * (leftPosition - slickWidth)}px`;
    }
}

let nextAction = (leftPosition,trackWidth,listWidth,slickWidth,track) => {
    if(leftPosition < (trackWidth - listWidth)) {
        track.style.left = `${-1 * (leftPosition + slickWidth)}px`;
    }
}

var inputs = document.getElementsByClassName('form-input');

for(var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener('keyup', function(){
        if(this.value.length >= 1) {
            this.nextElementSibling.classList.add('fijar');
        }
        else{
            this.nextElementSibling.classList.remove('fijar');
        }
    });
}
/*
function agregarServicio(ruta, servicio){
    console.log("agregar servicio " + servicio.nombre_Servicio + " a zona stage")

    $.ajax({
        method: "GET",
        url: ruta,
        cache: false
    })
    .done(function( respuesta ){
        $( "#stage" ).html( respuesta );
    });
}
*/

function agregarServicio(ruta){
    if(confirm('Desea agregar este serivicio al vehiculo?')){
        location.href = ruta
    }
}

function enviarAFacturas(ruta){
    if(confirm('Desea enviar este vehiculo a facturas?')){
        location.href = ruta
    }
}

function eliminarServicio(ruta){
    if(confirm('Esta seguro que desea quitar este servicio al vehiculo?')){
        location.href = ruta
    }
}