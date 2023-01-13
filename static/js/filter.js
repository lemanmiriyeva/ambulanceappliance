$(function () {
    var $grid = $('.grid').isotope({
        itemSelector: 'article',
        filter: '.main'
    });

    // filter buttons
    $('.filters-button-group').on('click', 'button', function () {
        var filterValue = $(this).attr('data-filter');
        $grid.isotope({ filter: filterValue });
    });
    $('.button-group').each(function (i, buttonGroup) {
        var $buttonGroup = $(buttonGroup);
        $buttonGroup.on('click', 'button', function () {
            $buttonGroup.find('.is-checked').removeClass('is-checked');
            $(this).addClass('is-checked');
        });
    });
});

// debounce so filtering doesn't happen every millisecond
function debounce(fn, threshold) {
    var timeout;
    return function debounced() {
        if (timeout) {
            clearTimeout(timeout);
        }
        function delayed() {
            fn();
            timeout = null;
        }
        timeout = setTimeout(delayed, threshold || 100);
    }
}

$(window).bind("load", function () {
    $('#all').click();
});





$(document).ready(function () {
  
    $("#owl-demo1").owlCarousel({
        items: 3,
        margin: 10,
        loop: true,
        autoplay: 2000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 2,
                nav: false
            },
            767: {
                items: 3,
                nav: false
            },
            1024: {
                items: 3,
                nav: false,
                loop: false
            },
            1500:{
                items: 4,
                nav: false,
                loop: false
            }
        }
    });
    $("#owl-demo2").owlCarousel({
        items: 3,
        margin: 10,
        loop: true,
        autoplay: 2000,
        responsiveClass: true,
        responsive: {
            0: {
                items: 3,
                nav: false
            },
            700: {
                items: 3,
                nav: false
            },
            1024: {
                items: 4,
                nav: false,
                loop: false
            },
            1500:{
                items: 5,
                nav: false,
                loop: false
            }
        }
    });
      
});
