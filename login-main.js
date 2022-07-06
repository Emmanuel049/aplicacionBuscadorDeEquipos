
// ------------------------- Codigo para cambiar de Login - Registro -------------------------

function mostrarRegistro(){
    let estado = document.getElementById("formularioDeRegistro");
    if (estado.style.display === "block") {
        estado.style.display = "none";
        document.getElementById("formularioDeLogueo").style.display = "none";
    } else {
        estado.style.display = "block";
        document.getElementById("formularioDeLogueo").style.display = "none";
    }
}
function mostrarLogin(){
    let estado = document.getElementById("formularioDeRegistro");
    if (estado.style.display === "block") {
        estado.style.display = "none";
        document.getElementById("formularioDeLogueo").style.display = "block";
    } else {
        estado.style.display = "none";
        document.getElementById("formularioDeLogueo").style.display = "block";
    }
}
function mostrarRegistroDePersona(){
    let estado = document.getElementById("formularioDeRegistroPersonal");
    if (estado.style.display === "block") {
        estado.style.display = "none";
        document.getElementById("formularioDeRegistro").style.display = "none";
    } else {
        estado.style.display = "block";
        document.getElementById("formularioDeRegistro").style.display = "none";
    }
}
function mostrarRegistroAnterior(){
    let estado = document.getElementById("formularioDeRegistro");
    if (estado.style.display === "block") {
        estado.style.display = "none";
        document.getElementById("formularioDeRegistroPersonal").style.display = "none";
    } else {
        estado.style.display = "block";
        document.getElementById("formularioDeRegistroPersonal").style.display = "none";
    }
}

function mandarDatosLogeo(){
    let usuario = document.getElementById("Usuario").value;
    let contraseña = document.getElementById("Contraseña").value;
    // console.log(usuario + " " + contraseña);
    // if (usuario === "Lucas" && contraseña === "asdasd123123") {
    //     window.open("index.html");
    //     window.close();
    // } else {
    //     alert("El Usuario o la Contraseña son invalidas");
    // }
}


// ------------------------- Codigo para Validar Formulario del Usuario -------------------------

document.addEventListener("DOMContentLoaded", function() {  // Cuando escuchamos el evento DOMContentLoaded creamos una funcion que..
    document.getElementById("formularioDeLogueo").addEventListener('submit', validarFormulario); 
});// en id del formulario se escucha el evento submit se crea otra funcion 

function validarFormulario(e) {
    e.preventDefault();
    let usuario = document.getElementById("Usuario").value;
    let contraseña = document.getElementById("Contraseña").value;

      if ( usuario == null || usuario.length == 0 || /^\s+$/.test(usuario) ){
          alert("Escribe un Usuario");
          return;
      }
       else{
        console.log(usuario);
        return;
      }

      this.submit();
  }


  
  const soloLetras = (e)=> {
    let tecla = window.Event ? e.which : e.teclaCode
    return (tecla <= 48 || tecla >= 57 && tecla != ":" )
}


 