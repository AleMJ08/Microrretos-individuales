const botonmagico = document.querySelector("#botonmagico");
const parrafo = document.querySelector("#parrafo");
const boton = document.querySelector("#btn-modo");

botonmagico.addEventListener("click", function() {
    parrafo.textContent = "Día fantástico para Alejandro! (Ref: AMJ)";
    parrafo.style.color = "orange";
    });

botonmagico.addEventListener("mouseenter", function() {
    botonmagico.textContent = "¡Púlsame, Muñoz!";
    botonmagico.style.fontSize = "30px";
    });

botonmagico.addEventListener("mouseleave", function() {
    botonmagico.textContent = "Cambiar ánimo";
    botonmagico.style.fontSize = "13px"
    });

boton.addEventListener("click", function() {
    document.body.classList.toggle("noche");
});