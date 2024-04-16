const closeModalButton = document.querySelector("#close-curriculum");
const info = document.querySelector("#info-project")
const fade = document.querySelector("#fade")
const principal = document.querySelector(".rightPages#about")
const left = document.querySelector(".left#about")


function showBackground(){
    principal.style.height = "";
    principal.style.opacity = "100%"
    left.style.display = "flex";
  }

const toggleModal = (openModalButton = null) => {
    if (openModalButton) {
      if (window.innerWidth < 1024){
        hideBackground()
      }
    } else {
      showBackground()
    }
    [info, fade].forEach((el)=> el.classList.toggle("hide"))
  }
  
  [closeModalButton, fade].forEach((el) => {
    el.addEventListener("click", () => toggleModal());
  });