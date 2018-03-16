$(function() {
    $('.premise-menu > a').hover(function() {
        $(this).fadeTo(0, 1);
    }, function() {
        $(this).fadeTo(0, .1);
    });

    $('.evidence-menu > a').hover(function() {
        $(this).fadeTo(0, 1);
    }, function() {
        $(this).fadeTo(0, .1);
    });
});