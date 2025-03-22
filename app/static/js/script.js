let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-item');

function showNextSlide() {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
}

setInterval(showNextSlide, 3000);

function navigateToLogin() {
    alert("Redirigiendo a la zona de logueo...");
    // Aquí podrías redirigir a otra página como 'window.location.href = "login.html"'
}
