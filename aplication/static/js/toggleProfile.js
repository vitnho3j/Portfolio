const info = document.querySelector("#info-profile")
const fade = document.querySelector("#fade")
const closeModalButton = document.querySelector("#close-info");
const person_name = document.querySelector("#person h1")
const person_occupation = document.querySelector("#person h2")
const profile_description = document.querySelector('#profile-description')
const profile_image = document.querySelector('#profile-information-image')




function getIdClicked(id){
    const openModalButton = document.querySelector(`#open-info-${id}`);
    toggleModal(openModalButton)
  };
  
  const toggleModal = (openModalButton = null) => {
    if (openModalButton) {
      person_name.innerHTML = openModalButton.getAttribute('profile-name')
      person_occupation.innerHTML = openModalButton.getAttribute('occupation')
      profile_description.innerHTML = openModalButton.getAttribute('description')
      if (openModalButton.getAttribute('photo')){
        profile_image.src = openModalButton.getAttribute('photo')
      }
      else {
        profile_image.src = "static/assets/no-photo.png"
      }
    }
    [info, fade].forEach((el)=> el.classList.toggle("hide"))
  }
  
  [closeModalButton, fade].forEach((el) => {
    el.addEventListener("click", () => toggleModal());
  });