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
// const template = document.getElementById('project-text-template')
const technologysDiv = document.querySelector("#project-technology");
const left = document.querySelector(".left#portfolio")
const principal = document.querySelector(".rightPages#portfolio")
const project_status = document.querySelector("#project-status")
let isZoomedIn = false;
var scrollPosition
var repository_link
var demo_link
var images
var currentZoom
var nextZoom
var nextZoomIndexs

document.addEventListener("DOMContentLoaded", (event) => {
  const projectButtons = document.querySelectorAll('.projectButtons');
  projectButtons.forEach(button => {
      button.addEventListener('click', (event) => {
        const id = event.target.getAttribute('data-id')
        getIdClicked(id)
      });
  });
});

function addZoomToImages() {
  const projectText = document.getElementById('project-text');
  images = projectText.getElementsByTagName('img');

  Array.from(images).forEach((img, index) => {
      window.zoomToDesktopImages(img, index)
  });
}

function addZoomToImagesMobile() {
  const projectText = document.getElementById('project-text');
  images = projectText.getElementsByTagName('img');

  Array.from(images).forEach((img, index) => {
      window.usePinchZoom(img, index)
  });
}

function getIdClicked (id){
  const openModalButton = document.querySelector(`#open-info-${id}`);
  scrollPosition = window.scrollY;
  toggleModal(openModalButton)
};

const sanatizeData = (data) => {
  const div = document.createElement('div');
  div.textContent = data
  return div.innerHTML; 
}

function setTextContent(element, content){
  return element.textContent = content
}

function setTechnologys(openModalButton = null){
  const technologysHTML = openModalButton.getAttribute('technologys')
  const technologysArray = technologysHTML.split(', ');
  technologysDiv.textContent = ""

  technologysArray.forEach(technology=>{
    div = document.createElement("div");
    setClassName(div, "technology-type")
    p = document.createElement("p")
    p.textContent = `${technology}`
    div.appendChild(p)
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

function setText(projectId){
  const template = document.getElementById(`project-text-template-${projectId}`)
  projectText.textContent = ''
  projectText.appendChild(template.content.cloneNode(true));
}


function setAttributes(openModalButton = null){
    setClassName(projectName, 'name-project-profile')
    setTextContent(projectName, openModalButton.getAttribute('name-project'))
    setSource(projectImage, openModalButton.getAttribute('image'))
    setTextContent(category, openModalButton.getAttribute('category'))
    setTextContent(demo, 'Clique aqui')
    setHref(demo, openModalButton.getAttribute('link') )
    setTextContent(repository, 'Clique aqui')
    setHref(repository, openModalButton.getAttribute('repository'))
    setTextContent(projectDescription, openModalButton.getAttribute('description'))
    setTechnologys(openModalButton)
    setText(openModalButton.getAttribute('data-id'))
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

function createRepositoryLinkFinalPart(openModalButton){
  const b_repository = document.createElement('b')
  const a_repository = document.createElement('a')
  setTextContent(a_repository, 'Repositório: ')
  a_repository.appendChild(b_repository)
  a_repository.href = `${openModalButton.getAttribute("repository")}`
  a_repository.target = "_blank"
  setTextContent(b_repository, `Clique aqui`)
  return a_repository
}

function createDemoLinkFinalPart(openModalButton){
  const b_demo = document.createElement('b')
  const a_demo = document.createElement('a')
  setTextContent(a_demo, "Demo: ")
  a_demo.appendChild(b_demo)
  a_demo.href = `${openModalButton.getAttribute("link")}`
  a_demo.target = "_blank"
  setTextContent(b_demo, `Clique aqui`)
  return a_demo
}

function setDivItemsFinalPart(div, a_repository, a_demo){
  const h1 = document.createElement('h1')
  const p = document.createElement('p')
  div.id = "lst-prt-div"
  div.appendChild(h1)
  div.appendChild(p)
  setTextContent(h1, 'Onde posso ver a demo/repositório deste projeto ?')
  setTextContent(p, `Você pode testar (caso haja uma demo) ou ver o código deste projeto (caso haja um repositório) no(s) link(s) abaixo:`)
  if (repository_link !== "None"){
    div.appendChild(a_repository)
  }
  if (demo_link !== "None"){
    div.appendChild(a_demo)
  }
  return div
}



function createFinalPartText(openModalButton){
  var div_final_part = document.createElement('div')
  const a_repository = createRepositoryLinkFinalPart(openModalButton)
  const a_demo = createDemoLinkFinalPart(openModalButton)
  div_final_part = setDivItemsFinalPart(div_final_part, a_repository, a_demo)
  projectText.appendChild(div_final_part);
}

function setVariablesFinalPart(openModalButton){
  repository_link = openModalButton.getAttribute("repository")
  demo_link = openModalButton.getAttribute("link")
}

function testRepository(openModalButton){
  setVariablesFinalPart(openModalButton)
  if (repository_link === 'None' && demo_link === 'None'){
    repository_paragraph.style.display = "none"
  } else {
    repository_paragraph.style.display = "block"
    createFinalPartText(openModalButton)
  }
}

function testStatus(openModalButton){
  var finished = openModalButton.getAttribute("finished")
  if (finished === "False"){
    setTextContent(project_status, "Projeto em andamento")
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
      addZoomToImagesMobile()
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





// function clearImgReferences(){
//   isZoomedIn = false;
//   currentZoom = 1;
//   nextZoom = 1;
//   nextZoomIndex = 1;
// }

// function imgAddEventListenerMouseLeave(img){
//   img.addEventListener("mouseleave", () => {
//     img.classList.remove("zoom-in");
//     img.classList.remove("zoom-out");
//     img.style.removeProperty('--x');
//     img.style.removeProperty('--y');
//     img.style.removeProperty('--zoom');
//     clearImgReferences();
//   });
// }

// function imgAddEventListenerMouseMove(img){
//   img.addEventListener("mousemove", (e) => {
//     if (isZoomedIn) {
//       const size = img.getBoundingClientRect();
//       const x = (e.clientX - size.left) / size.width * 100;
//       const y = (e.clientY - size.top) / size.height * 100;

//       img.style.setProperty('--x', x + '%');
//       img.style.setProperty('--y', y + '%');
//     }
//   });
// }

// function imgAddEventListenerClick(img, index) {
//   img.classList.add(`image-${index}`);
//   img.addEventListener("click", (e) => {
//     const size = img.getBoundingClientRect();
//     const x = (e.clientX - size.left) / size.width * 100;
//     const y = (e.clientY - size.top) / size.height * 100;

//     const zoomLevels = [1, 2, 3, 4];
//     currentZoom = parseFloat(img.style.getPropertyValue('--zoom')) || 1;
//     nextZoomIndex = (zoomLevels.indexOf(currentZoom) + 1) % zoomLevels.length;
//     nextZoom = zoomLevels[nextZoomIndex];

//     if (nextZoom === zoomLevels[zoomLevels.length - 1]) {
//       img.style.setProperty('cursor', 'zoom-out');
//     } else {
//       img.style.setProperty('cursor', 'zoom-in');
//     }

//     if (currentZoom === zoomLevels[zoomLevels.length - 1]) {
//       img.classList.remove("zoom-in");
//       img.classList.add("zoom-out");
//       img.style.setProperty('--zoom', 1);
//       console.log(img.classList)
//       isZoomedIn = false;
//     } else {
//       img.classList.add("zoom-in");
//       img.style.setProperty('--x', x + '%');
//       img.style.setProperty('--y', y + '%');
//       img.style.setProperty('--zoom', nextZoom);
//       console.log(img.classList)
//       isZoomedIn = true;
//     }
//   });
// }
