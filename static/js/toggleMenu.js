const closeModalButton = document.querySelector("#close-info");
const info = document.querySelector("#info-project")
const fade = document.querySelector("#fade")

const projectName = document.querySelector("#name-project-info")
const projectImage = document.querySelector("#project-image")
const category = document.querySelector("#category")
const demo = document.querySelector("#demo")
const projectDescription = document.querySelector("#project-description")
const projectText = document.querySelector("#project-text")


function getIdClicked(id){
  const openModalButton = document.querySelector(`#open-info-${id}`);
  toggleModal(openModalButton)
  
};

const toggleModal = (openModalButton = null) => {
  if (openModalButton) {
    projectName.innerHTML = openModalButton.getAttribute('name-project');
    projectImage.src = openModalButton.getAttribute('image')
    category.innerHTML = 'Category: ' + openModalButton.getAttribute('category');
    demo.innerHTML = openModalButton.getAttribute('demo')
    projectDescription.innerHTML = openModalButton.getAttribute('description')
    projectText.innerHTML = openModalButton.getAttribute('text')
  }
  [info, fade].forEach((el)=> el.classList.toggle("hide"))
}

[closeModalButton, fade].forEach((el) => {
  el.addEventListener("click", () => toggleModal());
});