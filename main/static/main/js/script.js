document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.querySelector(".toggle");
    const navLinks = document.querySelector(".navbar-links");

    toggle.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });
});

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        })
    })
})