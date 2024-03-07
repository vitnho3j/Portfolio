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

const toggleModal = (openModalButton = null) => {
  if (openModalButton) {
    projectName.className = 'name-project-profile'
    projectName.innerHTML = openModalButton.getAttribute('name-project');
    projectImage.src = openModalButton.getAttribute('image')
    category.innerHTML = openModalButton.getAttribute('category');
    demo.innerHTML = 'Click here'
    demo.setAttribute('href', openModalButton.getAttribute('link'))
    projectDescription.innerHTML = openModalButton.getAttribute('description')
    projectText.innerHTML = openModalButton.getAttribute('text')

    const technologysHTML = openModalButton.getAttribute('technologys')
    const technologysArray = technologysHTML.split(', ');
    technologysDiv.innerHTML = ''

    technologysArray.forEach(technology=>{
      div = document.createElement("div");
      div.classList.add("technology-type")
      div.innerHTML = `<p>${technology}`;
      technologysDiv.appendChild(div)
    })
  }
  [info, fade].forEach((el)=> el.classList.toggle("hide"))
}

[closeModalButton, fade].forEach((el) => {
  el.addEventListener("click", () => toggleModal());
});