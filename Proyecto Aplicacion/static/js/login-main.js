
// ------------------------- Codigo para cambiar de Login - Registro -------------------------

// function mostrarRegistro(){
//     let estado = document.getElementById("formularioDeRegistro");
//     if (estado.style.display === "block") {
//         estado.style.display = "none";
//         document.getElementById("formularioDeLogueo").style.display = "none";
//     } else {
//         estado.style.display = "block";
//         document.getElementById("formularioDeLogueo").style.display = "none";
//     }
// }
// function mostrarLogin(){
//     let estado = document.getElementById("formularioDeRegistro");
//     if (estado.style.display === "block") {
//         estado.style.display = "none";
//         document.getElementById("formularioDeLogueo").style.display = "block";
//     } else {
//         estado.style.display = "none";
//         document.getElementById("formularioDeLogueo").style.display = "block";
//     }
// }
// function mostrarRegistroDePersona(){
//     let estado = document.getElementById("formularioDeRegistroPersonal");
//     if (estado.style.display === "block") {
//         estado.style.display = "none";
//         document.getElementById("formularioDeRegistro").style.display = "none";
//     } else {
//         estado.style.display = "block";
//         document.getElementById("formularioDeRegistro").style.display = "none";
//     }
// }
// function mostrarRegistroAnterior(){
//     let estado = document.getElementById("formularioDeRegistro");
//     if (estado.style.display === "block") {
//         estado.style.display = "none";
//         document.getElementById("formularioDeRegistroPersonal").style.display = "none";
//     } else {
//         estado.style.display = "block";
//         document.getElementById("formularioDeRegistroPersonal").style.display = "none";
//     }
// }

// function mandarDatosLogeo(){
//     let usuario = document.getElementById("Usuario").value;
//     let contraseña = document.getElementById("Contraseña").value;
    // console.log(usuario + " " + contraseña);
    // if (usuario === "Lucas" && contraseña === "asdasd123123") {
    //     window.open("index.html");
    //     window.close();
    // } else {
    //     alert("El Usuario o la Contraseña son invalidas");
    // }
// }


// ------------------------- Codigo para Validar Usuario en Formulario de Logueo-------------------------

// cartelitoDelError.addEventListener("click",ocultarCartelitoDelError);
// function ocultarCartelitoDelError() {
//     document.getElementById("cartelitoDelError").style.display = "none"  
// }
// document.addEventListener("DOMContentLoaded", function() {  // Cuando escuchamos el evento DOMContentLoaded creamos una funcion que..
//     document.getElementById("formularioDeLogueo").addEventListener('submit', validarFormulario); 
// });// en id del formulario se escucha el evento submit se crea otra funcion 

// function validarFormulario(e) {
//     e.preventDefault();
//     let usuario = document.getElementById("Usuario").value;
//     let contraseña = document.getElementById("Contraseña").value;



//      if ( usuario == null || usuario.length == 0 || /^\s+$/.test(usuario)||
//        ( contraseña == null || contraseña.length == 0 || /^\s+$/.test(contraseña) ) ){
//         let mensaje = "Complete los Campos";
//         document.getElementById("cartelitoDelError").innerHTML = mensaje;

//       }
//        else {
//         console.log("Se escribio el Usuario: "+ usuario );
//         console.log("Se escribio la Contraseña: "+ contraseña );
//       }

//   }

 


//   const soloLetras = (e)=> {
//     let tecla = window.Event ? e.which : e.teclaCode;
//     return ((tecla <= 48 || tecla >= 57)||(tecla == 20) && (tecla !=(tecla <= 91)) )
// }
//Función que permite solo Números
// const validarTelefono = (ev)=> {
//  if ((ev.keyCode < 48) || (ev.keyCode > 57)) 
//   ev.returnValue = false;
// }
// ------------------------- Codigo para Validar Formulario del Usuario -------------------------

// document.addEventListener("keydown", (e)=> {
//     let Letra = e.key;
    
// });