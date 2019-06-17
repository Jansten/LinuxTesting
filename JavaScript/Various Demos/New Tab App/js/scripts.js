// A demo webpage for adding items to a list and storing the list in LocalStorage
// Based on code from this page: https://www.taniarascia.com/how-to-use-local-storage-with-javascript/

const form = document.querySelector('form')
const ul = document.querySelector('ul')
const button = document.querySelector('button')
const input = document.getElementById('item')
let itemsArray = localStorage.getItem('items') ? JSON.parse(localStorage.getItem('items')) : []

localStorage.setItem('items', JSON.stringify(itemsArray))
const data = JSON.parse(localStorage.getItem('items'))

const liMaker = text => {
  const li = document.createElement('li')
  li.textContent = text
  ul.appendChild(li)
}

form.addEventListener('submit', function(e) {
  e.preventDefault()

  itemsArray.push(input.value)
  localStorage.setItem('items', JSON.stringify(itemsArray))
  liMaker(input.value)
  input.value = ''
})

data.forEach(item => {
  liMaker(item)
})

button.addEventListener('click', function() {
  localStorage.clear()
  while (ul.firstChild) {
    ul.removeChild(ul.firstChild)
  }
})