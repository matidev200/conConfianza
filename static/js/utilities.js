var element_scroll = $(".msg-sended")
element_scroll.scrollTop(element_scroll.prop("scrollHeight"));


export function append_msg_to_dom(msg, sent_by_id, user_id) {
    if (sent_by_id === user_id) {
        // Crear un nuevo elemento de mensaje
        var message = `    <div class="message-container">
        <div class="message outgoing">
            <p class="message-text">${msg}</p>
            <span class="message-time">${getCurrentTime()}</span>
        </div>
    </div>`
    } else {
        var message = `    <div class="message-container">
        <div class="message">
            <p class="message-text"> ${msg}</p>
            <span class="message-time">${getCurrentTime()}</span>
        </div>
    </div>`
    }
    $('.msg-sended').append(message);

    element_scroll.scrollTop(element_scroll.prop("scrollHeight"));
}

export function getCurrentTime() {
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12;
    minutes = minutes < 10 ? '0' + minutes : minutes;
    var time = hours + ':' + minutes + ' ' + ampm;
    return time;
}