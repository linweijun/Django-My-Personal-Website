toastr.options.positionClass = 'toast-top-right';

//get CRSF
function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
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
//Get Times
function LocalDate() {
    var dates = new Date();
    return dates.toLocaleString()

}
$(document).ready(function() {
    //Login
    $(this).on('submit', '#form_login', function (e) {
        e.preventDefault();

        $.ajax({
            type: "POST",
            url: '',
            data: {
                username: $("#username").val(), password: $("#password").val(),
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            cache: false,

            success: function (json) {
                var resulr = json.url;
                if (json.status == 'success') {
                    toastr.success(json.message);
                    setTimeout("location.href= resulr ", 3000);
                } else {
                    toastr.error(json.message)
                }
            }
        })
    });

    //Register
    $(this).on('submit', '#form_register', function (e) {
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: '',
            data: {
                username: $('#username').val(), password: $('#password').val(),
                passowrd_confirm: $('#password_confirm').val(), email: $('#email').val()
            },
            cache: false,
            success: function (json) {
                var resulr = json.url;
                if (json.status == 'success') {
                    toastr.success(json.message);
                    setTimeout("location.href= resulr", 3000);
                } else {
                    toastr.error(json.message);
                }
            }
        })
    });
});