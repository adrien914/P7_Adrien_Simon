function send_message() {
    /*
    * This method gets the text that's in the input
    */
    const input = document.getElementById('message-input')
    const input_button = document.getElementById('message-button')
    const text = input.value // Get the input's value
    const element = `<user-chat text="${text}"></user-chat>` // create a new user chat with the value from the input
    const chat = $('#chat')[0]
    chat.innerHTML += element // Add the user-chat to the chat window
    // Disable the two inputs until the request is done
    input.setAttribute('disabled', "true")
    input_button.setAttribute('disabled', "true")
    chat.innerHTML += '<div class="loader"></div>'
    chat.scrollTop = chat.scrollHeight // Scroll to the bottom of the chat
    send_question(text).then(() => {
        // Reenable the inputs
        input.removeAttribute('disabled')
        input_button.removeAttribute('disabled')
        $('.loader').remove()
    })
}

function send_question(question) {
    /*
    * This function sends the question from the user to the backend, answers it and returns a promise
    * */
    return new Promise((resolve, reject) => {
        // send the question to the back-end
        $.ajax({
            url: "/send_question",
            type: "POST",
            contentType: "application/json",
            dataType: "json",
            data: JSON.stringify({
                "question": question
            }),
            success: function (data) {
                question_answer(data)
                resolve()
            },
            error: function (data) {
                alert("Erreur interne")
                resolve()
            }
        })
    })
}

async function question_answer(data) {
    chat = $('#chat')[0]
    // Réponse texte avec l'adresse
    let element = `<bot-chat text="Cet endroit se trouve à: ${data.text}"></bot-chat>`
    chat.innerHTML += element
    chat.scrollTop = chat.scrollHeight // Scroll to the bottom of the chat
    // Si les coordonnées ne sont pas vides
    if (data.map_location) {
        const longitude_latitude = [data.map_location.lat, data.map_location.lng]
        // On ajoute un chat du bot avec la carte dedans
        element = `<bot-chat text="Voici une carte pour te montrer l'endroit:" map_location="${longitude_latitude}"></bot-chat>`
        await sleep(2000)
        chat.innerHTML += element
        chat.scrollTop = chat.scrollHeight // Scroll to the bottom of the chat

    }
    if (data.wikipedia_summary) {
        element = `<bot-chat text="${data.wikipedia_summary}"></bot-chat>`
        await sleep(2000)
        chat.innerHTML += element
        chat.scrollTop = chat.scrollHeight // Scroll to the bottom of the chat
    }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

$(document).ready(function () {
    const input = document.getElementById('message-input')
    input.addEventListener("keypress", function (event){
        if (event.code === "Enter") {
            send_message()
        }
    })
})

