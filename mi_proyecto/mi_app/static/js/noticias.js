document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const filterDate = document.getElementById('filter-date');
    const newsCards = document.querySelectorAll('.noticia-card');
    const alertBox = document.getElementById('alert-box');

    // Función para mostrar la alerta
    function showAlert(message) {
        alertBox.textContent = message;
        alertBox.style.display = 'block';
        setTimeout(() => {
            alertBox.style.display = 'none';
        }, 3000); // La alerta desaparece después de 3 segundos
    }

    // Búsqueda en tiempo real
    searchInput.addEventListener('input', function () {
        const query = searchInput.value.toLowerCase();
        let hasResults = false;

        newsCards.forEach((card) => {
            const title = card.querySelector('h2').textContent.toLowerCase();
            if (title.includes(query)) {
                card.style.display = 'block';
                hasResults = true;
            } else {
                card.style.display = 'none';
            }
        });

        if (!hasResults) {
            showAlert('No se encontraron noticias para la búsqueda.');
        }
    });

    // Filtrado por fecha
    filterDate.addEventListener('change', function () {
        const selectedDate = new Date(filterDate.value);
        let hasResults = false;

        newsCards.forEach((card) => {
            const dateText = card.querySelector('.fecha').textContent.replace('Publicado el: ', '');
            const cardDate = new Date(dateText);

            if (selectedDate.toDateString() === cardDate.toDateString()) {
                card.style.display = 'block';
                hasResults = true;
            } else {
                card.style.display = 'none';
            }
        });

        if (!hasResults) {
            showAlert('No se encontraron noticias para la fecha seleccionada.');
        }
    });
});



document.addEventListener('DOMContentLoaded', function () {
    const newsCards = document.querySelectorAll('.noticia-card');

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        },
        { threshold: 0.1 }
    );

    newsCards.forEach((card) => {
        observer.observe(card);
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const backToTopButton = document.getElementById('back-to-top');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 200) {
            backToTopButton.classList.add('show');
        } else {
            backToTopButton.classList.remove('show');
        }
    });

    backToTopButton.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const carouselContainer = document.querySelector('.carousel-container');
    const items = document.querySelectorAll('.carousel-item');
    const prev = document.getElementById('prev');
    const next = document.getElementById('next');
    let index = 0;

    prev.addEventListener('click', function () {
        index = (index > 0) ? index - 1 : items.length - 1;
        updateCarousel();
    });

    next.addEventListener('click', function () {
        index = (index + 1) % items.length;
        updateCarousel();
    });

    function updateCarousel() {
        const offset = -index * 100;
        carouselContainer.style.transform = `translateX(${offset}%)`;
    }
});
