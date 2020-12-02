window.addEventListener('load', function() {

    new Glider(document.querySelector('.carousel-lista'), {
        slidesToShow: 1,
        slidesToScroll: 1,
        draggable: true,
        dots: '.carousel-indicadores',
        arrows: {
            prev: '.carousel-anterior',
            next: '.carousel-siguiente'
        },
        responsive: [{
            // screens greater than >= 775px
            breakpoint: 600,
            settings: {

                slidesToShow: '2',
                slidesToScroll: '2',
                itemWidth: 150,
                duration: 0.25
            }
        }, {
            // screens greater than >= 1024px
            breakpoint: 800,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 1,

            }
        }]
    });
});