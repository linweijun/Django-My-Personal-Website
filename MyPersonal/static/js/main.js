

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



$(document).ready(function() {
    toastr.options.positionClass = 'toast-top-right';
    //Login
    $(this).on('submit', '#login', function (e) {
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
                if(json.status == 'success') {
                    location.href = json.url;
                }else {
                    toastr.error(json.message)
                }
            }
        })
    });

    //Register
    $(this).on('submit', '#register', function (e) {
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: '',
            data: {
               username:$('#username').val(),password:$('#password').val(),
               password_confirm:$('#password-confirm').val(),
                email:$('#email').val(),
                csrfmiddlewaretoken: getCookie('csrftoken')
            },
            success:function (json) {
                if(json.url){
                    location.href=json.url;
                }else{
                    toastr.error(json.message);
                }
            }
        });

    });

    // Posts_CREATE


    //create_tags
    $(this).on('submit', '#create_tags', function (e) {
        e.preventDefault();

        $.ajax({
            type:'POST',
            url:'',
            data:{
                csrfmiddlewaretoken: getCookie('csrftoken'),
                tags: $('#tags').val(),
                meta_description:$('#meta_description').val()
            },
        })
    })




});
