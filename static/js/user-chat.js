class UserChat extends HTMLElement {
  constructor() {
    super()
    this.attachShadow({mode: 'open'})

    $(".animated-chat").removeClass("animated-chat")
    this.setAttribute('class', 'animated-chat')

    const linkElem = document.createElement('link')
    linkElem.setAttribute('rel', 'stylesheet')
    linkElem.setAttribute('href', 'static/css/index.css')

    const wrapper = document.createElement('div')
    wrapper.setAttribute('class','user-chat-div')

    const avatar = wrapper.appendChild(document.createElement('img'))
    avatar.setAttribute('class', 'avatar')
    avatar.src = 'static/images/anonymous.png'
    avatar.alt = 'Vous'

    this.message = wrapper.appendChild(document.createElement('p'))
    this.message.setAttribute('class','user-chat')



    this.shadowRoot.append(linkElem, wrapper)
  }

  connectedCallback() {
      this.message.textContent = this.getAttribute('text')
  }
}

customElements.define('user-chat', UserChat);
