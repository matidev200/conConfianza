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
    $(".reject-friend").on('click', function () {
        var $this = $(this)
        $.ajax({
            type: 'POST',
            url: `${host}/chat/delete-request/${$(this).attr('id')}`,
            success: function (response) {
                alert('Tu solicitud se rechazo correctamente :(.')
                $this.closest(".contact-bubble").hide()
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
            error: function (xhr, status, error) {
                alert('Ocurrio un error')
            }
        })
    })

    $(".accept-friend").on('click', function () {
        var $this = $(this)
        $.ajax({
            type: 'POST',
            url: `${host}/chat/accept-request/${$(this).attr('id')}`,
            success: function (response) {
                alert('Felicidades, ya son amigos :) .')
                $this.closest(".contact-bubble").hide()
            },
            data: {"is_approved": true},
            headers: {
                'X-CSRFToken': csrftoken
            },
            error: function (xhr, status, error) {
                alert('Ocurrio un error')
            }
        })
    })
})