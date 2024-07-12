const closeModalButton = document.querySelector("#close-info");
const info = document.querySelector("#info-project")
const fade = document.querySelector("#fade")
const projectName = document.querySelector("#name-project-info")
const projectImage = document.querySelector("#project-image")
const category = document.querySelector("p#content")
const demo = document.querySelector("#demo a")
const demo_paragraph = document.querySelector("#demo")
const repository = document.querySelector("#repository a")
const repository_paragraph = document.querySelector("#repository")
const projectDescription = document.querySelector("#project-description")
const projectText = document.querySelector("#project-text")
const technologysDiv = document.querySelector("#project-technology");
const left = document.querySelector(".left#portfolio")
const principal = document.querySelector(".rightPages#portfolio")
const project_status = document.querySelector("#project-status")
let isZoomedIn = false;
var scrollPosition


function imgAddEventListenerMouseLeave(img){
  img.addEventListener("mouseleave", () => {
    img.classList.remove("zoom-in");
    isZoomedIn = false;
});
}

function imgAddEventListenerMouseMove(img){
  img.addEventListener("mousemove", (e) => {
    if (isZoomedIn) {
        const size = img.getBoundingClientRect();
        const x = (e.clientX - size.left) / size.width * 100;
        const y = (e.clientY - size.top) / size.height * 100;

        img.style.setProperty('--x', x + '%');
        img.style.setProperty('--y', y + '%');
    }
});
}

function imgAddEventListenerClick(img, index){
  img.classList.add(`image-${index}`);
  img.addEventListener("click", (e) => {
      const size = img.getBoundingClientRect();
      const x = (e.clientX - size.left) / size.width * 100;
      const y = (e.clientY - size.top) / size.height * 100;

      if (img.classList.contains("zoom-in")) {
          img.classList.remove("zoom-in");
          isZoomedIn = false;
      } else {
          img.style.setProperty('--x', x + '%');
          img.style.setProperty('--y', y + '%');
          img.style.setProperty('--zoom', 2);
          img.classList.add("zoom-in");
          isZoomedIn = true;
      }
  });
}

function addZoomToImages() {
  const projectText = document.getElementById('project-text');
  const images = projectText.getElementsByTagName('img');

  Array.from(images).forEach((img, index) => {
      imgAddEventListenerClick(img, index)
      imgAddEventListenerMouseMove(img)
      imgAddEventListenerMouseLeave(img)
  });
}


function getIdClicked(id){
  const openModalButton = document.querySelector(`#open-info-${id}`);
  scrollPosition = window.scrollY;
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
    setInnerHTMLAtribute(repository, 'Clique aqui')
    setHref(repository, openModalButton.getAttribute('repository'))
    setInnerHTMLAtribute(projectDescription, openModalButton.getAttribute('description'))
    setInnerHTMLAtribute(projectText, openModalButton.getAttribute('text'))
    setTechnologys(openModalButton)
}

function hideBackground(){
  principal.style.height = "90px";
  principal.style.opacity = "0%"
  left.style.display = "none";
}

function showBackground(){
  principal.style.height = "";
  principal.style.opacity = "100%"
  left.style.display = "flex";
}

function testDemo(openModalButton){
  link = openModalButton.getAttribute('link')
  if (link === 'None'){
    demo_paragraph.style.display = "none"
  } else {
    demo_paragraph.style.display = 'block'
  }
}

function createFinalPartText(openModalButton){
  const div = document.createElement('div')
  const h1 = document.createElement('h1')
  const p = document.createElement('p')
  const b = document.createElement('b')
  const a = document.createElement('a')
  a.appendChild(b)
  a.href = `${openModalButton.getAttribute("repository")}`
  div.appendChild(h1)
  div.appendChild(p)
  div.appendChild(a)
  setClassName(div, 'prt-txt-final-part')
  setInnerHTMLAtribute(h1, 'Onde posso testar o projeto ?')
  setInnerHTMLAtribute(p, `Você pode testar este projeto no link abaixo:`)
  setInnerHTMLAtribute(b, `${openModalButton.getAttribute("repository")}`)
  projectText.appendChild(div);
}

function testRepository(openModalButton){
  link = openModalButton.getAttribute("repository")
  if (link === 'None'){
    repository_paragraph.style.display = "none"
  } else {
    repository_paragraph.style.display = "block"
    createFinalPartText(openModalButton)
  }
}

function testStatus(openModalButton){
  var finished = openModalButton.getAttribute("finished")
  if (finished === "False"){
    setInnerHTMLAtribute(project_status, "Projeto em andamento")
    project_status.style.display = 'block'
  } else {
    project_status.style.display = 'none'
  }
}

const toggleModal = (openModalButton = null) => {
  if (openModalButton) {
    testStatus(openModalButton)
    testDemo(openModalButton)
    setAttributes(openModalButton)
    testRepository(openModalButton)
    addZoomToImages()
    if (window.innerWidth <= 1024){
      hideBackground()
    }
  } else {
    showBackground()
  }
  window.scrollTo(0, scrollPosition);
  [info, fade].forEach((el)=> el.classList.toggle("hide"))
}

[closeModalButton, fade].forEach((el) => {
  el.addEventListener("click", () => toggleModal());
});