

 function cargarPagina() {
    // Creamos unas variables con los años
    let anioMinimo = 1900;
    let anioMaximo = 2020;
    let anio = 0;

    let comboAnio = document.getElementById("anio");

    for (let i = anioMinimo; i <= anioMaximo; i++) {
        let option = document.createElement("option"); //Con esto creo la etiqueta option
        option.setAttribute("value", i); //Con esto le seteo el valor (pero de forma interna, el usuario no ve este valor)

        let optionText = document.createTextNode(i); //Con esto le seteo la opción que yo como usuario veo
        option.appendChild(optionText); //Con esto meto el optionText en la etiqueta Option
        comboAnio.appendChild(option); //Con esto meto el option en el comboAnio, que es lo que está vinculado a la etiqueta
    }

    let array = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]; //Le meto todos los meses y hago lo mismo

    let comboMes = document.getElementById("mes");

    for (let i = 1; i <= array.length; i++) {
        let option=document.createElement("option"); //Con esto le creo la etiqueta option
        option.setAttribute("value", i);
        option.setAttribute("placeholder", "Mes"); //Con esto le seteo el valor (pero de forma interna, el usuario no ve este valor)
        let itexto="";

        switch(i){
            case 1: itexto="Enero";
            break;
            case 2: itexto="Febrero";
            break;
            case 3: itexto="Marzo";
            break;
            case 4: itexto="Abril";
            break;
            case 5: itexto="Mayo";
            break;
            case 6: itexto="Junio";
            break;
            case 7: itexto="Julio";
            break;
            case 8: itexto="Agosto";
            break;
            case 9: itexto="Septiembre";
            break;
            case 10: itexto="Octubre";
            break;
            case 11: itexto="Noviembre";
            break;
            case 12: itexto="Diciembre";
            break;
        }

        let optionText=document.createTextNode(itexto); //Con esto le seteo la opción que yo como usuario veo
        option.appendChild(optionText); //Con esto meto el optionText en la etiqueta Option
        comboMes.appendChild(option); //Con esto meto el option en el comboMes, que es lo que está vinculado a la etiqueta  
    }

    //Cuando pulso año o mes lanza un evento Onchange que calcula el número de días del mes (CalcularDiasMes).
    //Tras esto, creo un objeto Date con los valores del select.
    //Ya con el objeto Date, lo muestro en pantalla con date.InnerHTML() y hecho
}

function cargarNumeroDias(){
    let comboDia=document.getElementById("dia");
    var length = comboDia.options.length;
    for (i = comboDia.length - 1; i >= 0; i--) {
        comboDia.remove(i);
    }

    let anio = document.getElementById("anio").value;
    let mes = document.getElementById("mes").value;

    let numeroDias=calcularDiasMes(anio, mes); //Con esto cojo el número de días para el mes y el año en concreto

    for (let i= 1; i <= numeroDias; i++) {
        let option=document.createElement("option"); //Con esto le creo la etiqueta option
        option.setAttribute("value", i); //Con esto le seteo el valor (pero de forma interna, el usuario no ve este valor)
        let optionText=document.createTextNode(i); //Con esto le seteo la opción que yo como usuario veo
        option.appendChild(optionText); //Con esto meto el optionText en la etiqueta Option
        comboDia.appendChild(option); //Con esto meto el option en el comboDia, que es lo que está vinculado a la etiqueta  
    }
}

function calcularDiasMes(anio, mes) {
    let numeroDias = -1;

    switch (mes) {
        case '1':
        case '3':
        case '5':
        case '7':
        case '8':
        case '10':
        case '12':
            numeroDias = 31;
            break;
        case '4':
        case '6':
        case '9':
        case '11':
            numeroDias = 30;
            break;
        case '2':
            if ((anio % 4 == 0 && anio % 100 != 0) || (anio % 100 == 0 && anio % 400 == 0)) { //Con esto sé si es bisiesto o no
                numeroDias = 29;
            } else {
                numeroDias = 28;
            }
            break;
    }

    return numeroDias;
}

window.onload = cargarPagina; //Para que esta función se cargue cuando se inicia la página