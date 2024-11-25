function ValidarFormulario() {
  let name = document.getElementById("nombre").value.trim();
  let correo = document.getElementById("correo").value.trim();
  let comentarios = document.getElementById("text").value.trim();

  const custom_alert_false = document.getElementById("custom_alert_false");

  // Validación de campos vacíos
  if (name === "" || correo === "" || comentarios === "") {
    custom_alert_false.classList.add("active");
    return false;
  } else if (!validateEmail(correo)) {
    alert("Por favor, introduce un correo válido.");
    return false;
  } else {
    document
      .getElementById("contactform")
      .addEventListener("submit", function (event) {
        event.preventDefault();
        const alert_true = document.getElementById("alert_true");
        alert_true.classList.add("show");
        setTimeout(
          () => {
            alert_true.classList.remove("show");
          },
          4000,
          limpiar_input()
        );
      });
  }
}

function limpiar_input() {
  document.getElementById("nombre").value = "";
  document.getElementById("correo").value = "";
  document.getElementById("text").value = "";
}
function closeCustomAlert_false() {
  document.getElementById("custom_alert_false").classList.remove("active");
}

// Función para validar el formato del correo electrónico
function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}
