$(document).ready(function(){
    $('#menu').find('#tag').hover(function() {
        $(this).addClass('menu-l');
        $('#sub-menu',this).stop().slideDown('1000');
    },function() {
        $(this).removeClass('menu-l');
        $('#sub-menu',this).stop().slideUp('1000');
    });
});