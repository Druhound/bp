$(document).ready(function() {
       $("#form").submit(function(event){
            $.ajax({
                url : this.action,
                type : "POST",
                cache:false,
                dataType:'text',
                data : {
                    form : $('#form').val()
                },
                success: function () {
                    $('message').html("<h2>Submit</h2>")
                }
            });
            return false;
       });
});



// CSRF code
function getCookie(name) {
    var cookieValue = null;
    var i = 0;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (i; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');