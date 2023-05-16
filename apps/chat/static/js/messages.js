import { append_msg_to_dom } from './utilities.js';

let loc = window.location
let wsStart = 'ws://'

const USER_ID = parseInt($("#user-id").val());

if (loc.protocol === 'https') {
    wsStart = 'wss://'
}

let endpoint = wsStart + loc.host + loc.pathname

var socket = new WebSocket(endpoint)

// Send the websocket data to server
socket.onopen = async function(e) {
    $('#msg-form').on('submit', function (e) {

        e.preventDefault();
        var msg = $('#msg').val();
        let send_to = parseInt($(".thread_send_to_id").attr('id'))
        let thread_id = parseInt($(".thread_id").attr('id'))

        // Proccess the data
        let data = {
            'message': msg,
            'sent_by': USER_ID,
            'send_to': send_to,
            'thread_id': thread_id
        }

        data = JSON.stringify(data)
        socket.send(data)
        // Clear input when msg is sended
        $('#msg').val('');

    });
}

socket.onmessage = async function (e) {
    let data = JSON.parse(e.data)
    let message = data['message']
    let sent_by_id = data['sent_by']
    append_msg_to_dom(message, sent_by_id, USER_ID)

}
socket.onerror = async function (e) {
}
socket.onclose = async function (e) {
}

