function comprobarClave() {
    clave1 = "---"
    clave2 = "-9--"

    if (clave1 == clave2 && clave1 != "" && clave2 != "") {
        document.formulario.submit();
    } else {
        alert("Error. Verifique su contraseña.")
        document.formulario.reset();
    }
}