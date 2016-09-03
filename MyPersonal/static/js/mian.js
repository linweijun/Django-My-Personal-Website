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
    var dates = new Date()
    return dates.toLocaleString()

}
$(document).ready(function(){
 $(this).on('submit', '#login', function (e) {
                toastr.options.positionClass = 'toast-top-right';
                e.preventDefault();

                $.ajax({
                    type: 'POST',
                    url: '',
                    data: {
                        username: $("#username").val(), password: $("#password").val(),
                        csrfmiddlewaretoken: getCookie('csrftoken')
                    },
                    cache: false,

                    success:function (json) {
                        resulr = json.url;
                       if (json.success == 'success'){
                        toastr.success('登陆成功');
                          setTimeout("location.href= resulr ", 3000);
                        }else {
                            toastr.error(json)
                       }
                    }

                })
            });
 });