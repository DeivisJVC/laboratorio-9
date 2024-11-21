function Bienvenido() {
  alert("Bienvenido a mi pagina");
}

function ValidarFormulario() {
  const form = document.getElementById("contactform");
  const name = document.getElementById("nombre").value;
  const correo = document.getElementById("correo");
  const comentarios = document.getElementById("text").value;
  if (name == "" || correo == "" || comentarios == "") {
    alert("Por favor, debes completar todos los campos");
    return false;
  } else {
    alert("Formulario Enviado Correctamente");
    return true;
  }
}
