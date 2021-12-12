function update(id) {
    const element = document.getElementById(id)
    const parent = element.parentElement
    const clone_element = element.cloneNode(true)
    element.remove()
    parent.appendChild(clone_element)
}
