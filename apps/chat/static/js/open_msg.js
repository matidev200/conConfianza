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
    $(".send-button").on('click', function () {
        var $this = $(this)
        $.ajax({
            type: 'POST',
            url: `${host}/chat/set_last_person_msg/`,
            data: { last_person_chat: parseInt($this.attr('id')) },
            success: function (response) {
                window.location = "/chat/"
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
            error: function (xhr, status, error) {
                alert('Ocurrio un error')
            }
        })
    })
})