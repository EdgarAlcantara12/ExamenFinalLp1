document.addEventListener("DOMContentLoaded", function () {
    const herramientaItems = document.querySelectorAll('.nombre-herramienta');
    const modal = document.getElementById('herramienta-modal');
    const closeButton = document.querySelector('.close');

    // Mostrar el modal con los detalles de la herramienta
    herramientaItems.forEach(item => {
        item.addEventListener('click', function () {
            const nombre = item.getAttribute('data-nombre');
            const descripcion = item.getAttribute('data-descripcion');
            const enlace = item.getAttribute('data-enlace');
            const imagen = item.getAttribute('data-imagen');

            // Asignar los valores al modal
            document.getElementById('modal-title').textContent = nombre;
            document.getElementById('modal-description').textContent = descripcion;
            const modalImage = document.getElementById('modal-image');
            modalImage.src = imagen;
            modalImage.style.display = 'block'; // Mostrar imagen si existe

            // Si no hay imagen, ocultarla
            if (!imagen) {
                modalImage.style.display = 'none';
            }

            document.getElementById('modal-link').href = enlace;

            // Mostrar el modal
            modal.style.display = 'flex';
        });
    });

    // Cerrar el modal
    closeButton.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    // Cerrar el modal si se hace clic fuera de él
    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
