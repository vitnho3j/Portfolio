const closeModalButton = document.querySelector("#close-curriculum");
const info = document.querySelector("#info-project")
const fade = document.querySelector("#fade-about")
const principal = document.querySelector(".rightPages#about")
const left = document.querySelector(".left#about")

const toggleModal = () => {
  [info, fade].forEach((el)=> el.classList.toggle("hide"))
}
  
[closeModalButton, fade].forEach((el) => {
  el.addEventListener("click", () => toggleModal());
});