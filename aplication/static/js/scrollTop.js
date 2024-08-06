document.addEventListener("DOMContentLoaded", (event) => {
    const buttonToTop = document.querySelector('#scrollTop');
    buttonToTop.addEventListener('click', (event) => {
        scrollToTop()
    });
});

function scrollToTop(){
    var div = document.getElementById('begin');
    div.style.scrollBehavior = "smooth"
    div.scrollTop = 0
}

