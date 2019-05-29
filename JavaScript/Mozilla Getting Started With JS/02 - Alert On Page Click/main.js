// Displays a browser pop-up when you click anywhere on the page

document.querySelector('html').onclick = function() {
    alert('Ouch! Stop poking me!');
}