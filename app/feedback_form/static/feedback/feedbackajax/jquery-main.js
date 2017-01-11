$(document).ready(function() {
       $("#form").submit(function(event){
            $.ajax({
                url : null,
                type : "POST",
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