$(document).ready(function() {
    if ($(window).width() <= 800) {
        $("#all-other-events").removeClass("container-fluid");
        $("#all-other-events").addClass("container");
    }

    $(window).resize(function() {
        // If browser is resized, check width again
        if ($(window).width() <= 800) {
            $("#all-other-events").removeClass("container-fluid");
            $("#all-other-events").addClass("container");
        } else {
            $("#all-other-events").removeClass("container");
            $("#all-other-events").addClass("container-fluid");
        }
    });

    let right = document.getElementById('all-events-section').clientHeight;
    
    if ($(window).width() > 800) {
        document.getElementById('featured-events-section').style.height = right;
    }
});