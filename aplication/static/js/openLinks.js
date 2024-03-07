const button = document.querySelector("#open-links")

function startedClose(){
    var div = document.querySelector(".profile-socials");
    div.style.display = "none";
}

function cleanInnerDivButton(){
    button.innerHTML = ''
}

function getcomputedStyle(div = null) {
    var computedStyle = window.getComputedStyle(div);
    return computedStyle
}

function createParagraph(){
    p = document.createElement("p")
    return p
}

function openDiv(div = null){
    div.classList.remove("animation-reverse-items");
    div.style.display = "flex"
}

function closeDiv(div = null){
    div.classList.remove('animation-items');
    div.classList.add("animation-reverse-items");
    setTimeout(() => {
        div.style.display = "none";
    }, 300); 
}

function changeTextParagraph(paragraph = null, text){
    paragraph.innerHTML = text
}

function appendChild(paragraph = null){
    button.appendChild(paragraph)
}

function toggleDiv() {
    cleanInnerDivButton()
    p = createParagraph()
    var div = document.querySelector(".profile-socials");
    var computedStyle = getcomputedStyle(div)
    if (computedStyle.display === "none") {
        openDiv(div)
        changeTextParagraph(p, 'Esconder Contatos')
    } else {
        closeDiv(div)
        changeTextParagraph(p, 'Mostrar Contatos')
    }
    appendChild(p)
}

