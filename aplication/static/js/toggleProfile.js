const info = document.querySelector("#info-profile")
const fade = document.querySelector("#fade")
const closeModalButton = document.querySelector("#close-info");
const socials = document.querySelector("#socials")
const profile_name=document.querySelector("#profile-name")
const occupation = document.querySelector("#occupation")
const description = document.querySelector("#description")
const photo = document.querySelector("#photo")



function getIdClicked(id){
    const openModalButton = document.querySelector(`#open-info-${id}`);
    toggleModal(openModalButton)
    
  };
  
  const toggleModal = (openModalButton = null) => {
    if (openModalButton) {

    }
    [info, fade].forEach((el)=> el.classList.toggle("hide"))
  }
  
  [closeModalButton, fade].forEach((el) => {
    el.addEventListener("click", () => toggleModal());
  });