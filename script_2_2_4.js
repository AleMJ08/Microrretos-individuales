const botonmagico = document.querySelector("#botonmagico");
const parrafo = document.querySelector("#parrafo");

botonmagico.addEventListener("click", function() {
    parrafo.textContent = "Día fantástico para Alejandro! (Ref: AMJ)";
    parrafo.style.color = "orange";
    });

botonmagico.addEventListener("mouseenter", function() {
    botonmagico.textContent = "¡Púlsame, Muñoz!";
    parrafo.
    });

botonmagico.addEventListener("mouseleave", function() {
    botonmagico.textContent = "Cambiar ánimo";
    });