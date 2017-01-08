// http://stackoverflow.com/questions/13437446/how-to-display-selected-item-in-bootstrap-button-dropdown-title
$(".dropdown-menu li a").click(function(){
    $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="caret"></span>');
    $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
});