/*SCRIPTS PARA INDEX.HTML */
let currentIndex = 0;
const items = document.querySelectorAll(".carousel-item");

function updateCarousel() {
    items.forEach((item, index) => {
        item.classList.toggle("active", index === currentIndex);
    });
}

function moveCarousel(direction) {
    currentIndex += direction;
    if (currentIndex < 0) {
        currentIndex = items.length - 1;
    } else if (currentIndex >= items.length) {
        currentIndex = 0;
    }
    updateCarousel();
}

// Inicializa el carrusel
updateCarousel();
