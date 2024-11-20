function validarFormulario() {
  let nombre = document.getElementById("nombre").value;
  let email = document.getElementById("correoElectronico").value;
  let imagen = document.getElementById("file");
  if (nombre == "" || email == "" || imagen == "") {
    alert("Todos los campos son obligatorios");
    return false;
  }
  return true;
}
function mostrarImagen(event) {
  let imagen = document.getElementById("ver-img");
  imagen.src = URL.createObjectURL(event.target.files[0]); //Recuerda la s en files
}
