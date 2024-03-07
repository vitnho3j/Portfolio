const closeModalButton = document.querySelector("#close-info");
const info = document.querySelector("#info-project")
const fade = document.querySelector("#fade")

const projectName = document.querySelector("#name-project-info")
const projectImage = document.querySelector("#project-image")
const category = document.querySelector("p#content")
const demo = document.querySelector("#demo a")
const projectDescription = document.querySelector("#project-description")
const projectText = document.querySelector("#project-text")
const technologysDiv = document.querySelector("#project-technology");


function getIdClicked(id){
  const openModalButton = document.querySelector(`#open-info-${id}`);
  toggleModal(openModalButton)
  
};

function setInnerHTMLAtribute(element, innerHtml){
    return element.innerHTML = innerHtml
}

function setTechnologys(openModalButton = null){
  const technologysHTML = openModalButton.getAttribute('technologys')
  const technologysArray = technologysHTML.split(', ');
  setInnerHTMLAtribute(technologysDiv, '')

  technologysArray.forEach(technology=>{
    div = document.createElement("div");
    setClassName(div, "technology-type")
    setInnerHTMLAtribute(div, `<p>${technology}`)
    technologysDiv.appendChild(div)
  })
}

function setSource(element, src){
  element.src = src
}

function setHref(element, href){
  element.setAttribute('href', href)
}

function setClassName(element, className){
  element.className = className
}

function setAttributes(openModalButton = null){
    setClassName(projectName, 'name-project-profile')
    setInnerHTMLAtribute(projectName, openModalButton.getAttribute('name-project'))
    setSource(projectImage, openModalButton.getAttribute('image'))
    setInnerHTMLAtribute(category, openModalButton.getAttribute('category'))
    setInnerHTMLAtribute(demo, 'Clique aqui')
    setHref(demo, openModalButton.getAttribute('link') )
    setInnerHTMLAtribute(projectDescription, openModalButton.getAttribute('description'))
    setInnerHTMLAtribute(projectText, openModalButton.getAttribute('text'))
    setTechnologys(openModalButton)
}

const toggleModal = (openModalButton = null) => {
  if (openModalButton) {
    setAttributes(openModalButton)
  }
  [info, fade].forEach((el)=> el.classList.toggle("hide"))
}

[closeModalButton, fade].forEach((el) => {
  el.addEventListener("click", () => toggleModal());
});