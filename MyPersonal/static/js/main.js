

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
$(document).ready(function() {
    toastr.options.positionClass = 'toast-top-right';
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
                if (json.status == 'success') {
                    toastr.success(json.message);
                    setTimeout(location.href= json.url, 3000);
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
            type: "POST",
            url: '',
            data: {
               username:$('#username').val(),password:$('#password').val(),
               password_confirm:$('#password_confirm').val(),
                email:$('#email').val(),
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            cache: false,

            success: function (json) {
                var resulr = json.url;
                if (json.status == 'success') {
                    toastr.success(json.message);
                } else {
                    toastr.error(json.message)
                }
            }
        })

    });

    // Article_CREATE
    $(this).on('submit', '#form_article', function (e) {
        e.preventDefault();

        $.ajax({
            type:'POST',
            url:'',
            data:{
                csrfmiddlewaretoken: getCookie('csrftoken'),
                title:$('#title').val(),
                content:$('#content').val(),
                tags:$('#tags').val(),
                classic:$('#classic').val()
            },

            success:function (json) {
                if (json.status == 'success'){
                    toastr.success(json.message)
                }else{
                    toastr.error(json.message)
                }
            }
        })
    })


});
