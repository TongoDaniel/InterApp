document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('section:not(:first-child)');
    sections.forEach(section => {
        section.classList.add('section-hidden');
    });
    const sectionObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('section-show');
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        threshold: 0.15
    });
    sections.forEach(section => {
        sectionObserver.observe(section);
    });
// Handle carousel navigation
    const carouselNavButtons = document.querySelectorAll('.carousel-nav-button');
    carouselNavButtons.forEach(button => {
        button.addEventListener('click', function () {
            const carouselId = this.getAttribute('data-carousel');
            const direction = this.getAttribute('data-direction');
            const carousel = document.getElementById(carouselId);
            const scrollAmount = direction === 'next' ?
                carousel.offsetWidth * 0.8 :
                -carousel.offsetWidth * 0.8;
            carousel.scrollBy({
                left: scrollAmount,
                behavior: 'smooth'
            });
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
// Handle carousel indicators
    const carouselIndicators = document.querySelectorAll('.carousel-indicator');
    carouselIndicators.forEach(indicator => {
        indicator.addEventListener('click', function () {
            const carouselId = this.getAttribute('data-carousel');
            const index = parseInt(this.getAttribute('data-index'));
            const carousel = document.getElementById(carouselId);
// Update active indicator
            document.querySelectorAll(`.carousel-indicator[data-carousel="${carouselId}"]`)
                .forEach(ind => ind.classList.remove('active'));
            this.classList.add('active');
// Calculate scroll position
            const scrollAmount = carousel.scrollWidth * (index / 3);
            carousel.scrollTo({
                left: scrollAmount,
                behavior: 'smooth'
            });
        });
    });
// Set initial active indicators
    const carousels = document.querySelectorAll('.carousel');
    carousels.forEach(carousel => {
        const carouselId = carousel.id;
        const firstIndicator = document.querySelector(`.carousel-indicator[data-carousel="${carouselId}"][data-index="0"]`);
        if (firstIndicator) {
            firstIndicator.classList.add('active');
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
// Handle scroll events to update indicators
    const carousels = document.querySelectorAll('.carousel');
    carousels.forEach(carousel => {
        carousel.addEventListener('scroll', function () {
            const carouselId = this.id;
            const scrollPosition = this.scrollLeft;
            const maxScroll = this.scrollWidth - this.clientWidth;
            const scrollPercentage = scrollPosition / maxScroll;
// Calculate which indicator should be active
            let activeIndex = 0;
            if (scrollPercentage > 0.66) {
                activeIndex = 2;
            } else if (scrollPercentage > 0.33) {
                activeIndex = 1;
            }
// Update indicators
            document.querySelectorAll(`.carousel-indicator[data-carousel="${carouselId}"]`)
                .forEach((indicator, index) => {
                    if (index === activeIndex) {
                        indicator.classList.add('active');
                    } else {
                        indicator.classList.remove('active');
                    }
                });
        });
    });
});