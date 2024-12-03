

// Cards Video Activity

document.addEventListener("DOMContentLoaded", function() {
   // Selecciona todas las tarjetas
   const cards = document.querySelectorAll('.Card');

   // Recorre cada tarjeta
   cards.forEach(card => {
      // Selecciona el video dentro de la tarjeta
      const video = card.querySelector('video');
      
      // Define el tiempo en el que debe quedarse antes de reproducirse
      const startTime = 7.2;  // Cambia esto por el tiempo en segundos (por ejemplo, 5 segundos)
      
      // Pausa el video al inicio y lo pone en el tiempo específico
      video.pause();
      video.currentTime = startTime;  // Cambia esto para el fotograma deseado
      
      // Reproduce el video cuando el mouse pasa sobre la tarjeta
      card.addEventListener('mouseover', () => {
         video.play();  // Reproducir cuando el mouse entra
      });
      
      // Pausa el video y lo reinicia al tiempo especificado cuando el mouse se aleja
      card.addEventListener('mouseout', () => {
         video.pause();  // Pausar cuando el mouse sale
         video.currentTime = startTime;  // Volver al tiempo específico
      });
   });
});


// Modals Login - Register

// Botones
const btnLogin = document.getElementById("IniciarSesion-hero");
const btnRegister = document.getElementById("Registrarse-hero");

// Contenedor de los modales
const modalsContainer = document.getElementById("modals-container");

// Función para cargar un modal desde una URL
const loadModal = (url) => {
  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Error al cargar el modal");
      }
      return response.text();
    })
    .then((html) => {
      modalsContainer.innerHTML = html;
      const modal = document.querySelector(".modal");
      modal.style.display = "flex";

      // Cerrar el modal al hacer clic en el botón de cerrar
      const closeBtn = modal.querySelector(".close");
      closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
        modalsContainer.innerHTML = ""; // Limpia el contenido del modal
      });
    })
    .catch((error) => console.error("Error cargando el modal:", error));
};

// Eventos para cargar los modales desde las rutas Django
btnLogin.addEventListener("click", () => loadModal("/justa/login-modal/"));
btnRegister.addEventListener("click", () => loadModal("/justa/register-modal/"));
