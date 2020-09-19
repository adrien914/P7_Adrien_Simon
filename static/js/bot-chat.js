class BotChat extends HTMLElement {
  constructor() {
    super()
    this.attachShadow({mode: 'open'})

    $(".animated-chat").removeClass("animated-chat")
    this.setAttribute('class', 'animated-chat')

    const linkElem = document.createElement('link')
    linkElem.setAttribute('rel', 'stylesheet')
    linkElem.setAttribute('href', 'static/css/index.css')
    this.wrapper = document.createElement('div')
    this.wrapper.setAttribute('class','bot-chat-div')

    this.message = this.wrapper.appendChild(document.createElement('p'))
    this.message.setAttribute('class','bot-chat')

    const avatar = this.wrapper.appendChild(document.createElement('img'))
    avatar.setAttribute('class', 'avatar')
    avatar.alt = 'Papy'
    avatar.src = 'static/images/granpy.png'

    this.shadowRoot.append(linkElem, this.wrapper)

  }

  connectedCallback() {
      // put the text given in the attributes in the paragraph's text
      this.message.textContent = this.getAttribute('text')
      // Get the map location from the attributes
      const map_location = this.getAttribute('map_location')
      // If a map location was given
      if (map_location) {
        // create a new div for the map in the message
        const map = this.message.appendChild(document.createElement('div'))
        // Give it an id of 'map', there wont be any id conflict because it's in the shadow root
        map.setAttribute('id', "map")
        // Give it the map_class class to style it
        map.setAttribute('class', 'map')
        // Format the coordinates from the map location
        const coordinates = map_location.split(",")
        const latitude = parseFloat(coordinates[0])
        const longitude = parseFloat(coordinates[1])
        // Initialize the map at the right latitude and longitude
        const gmap = new google.maps.Map(this.shadowRoot.getElementById("map"), {
          center: { lat: latitude, lng: longitude},
          zoom: 8
        })
        // Put a new marker on the map at the point of interest
        new google.maps.Marker({
            position: {lat: latitude, lng: longitude},
            map: gmap
        })
      }
  }
}

customElements.define('bot-chat', BotChat);
