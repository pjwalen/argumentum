$(function() {
    $('.premise').mouseover(function() {
        $(this).children('.premise-menu').show();
    });

    $('.premise').mouseleave(function() {
        $(this).children('.premise-menu').hide();
    });

    $('.evidence').mouseover(function() {
        $(this).children('.evidence-menu').show();
    });

    $('.evidence').mouseleave(function() {
        $(this).children('.evidence-menu').hide();
    });
});