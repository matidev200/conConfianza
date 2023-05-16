let host = window.location.origin
// using jQuery
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
var csrftoken = getCookie('csrftoken');
$(document).ready(function () {
    
    $(".add-friend").on('click', function () {
        $.ajax({
            type: 'POST',
            url: `${host}/chat/add-contacts/`,
            data: { 'user_to_request': parseInt($(this).attr('id')), 'user': parseInt($(".user-id").attr('id')) },
            success: function (response) {
                alert('Tu solicitud se envio correctamente !')
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
            error: function (xhr, status, error) {
                alert('Tu solicitud fue enviada o ya son amigos.')
            }
        })
    })
})