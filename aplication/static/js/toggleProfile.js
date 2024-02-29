const info = document.querySelector("#info-profile")
const fade = document.querySelector("#fade")
const closeModalButton = document.querySelector("#close-info");
const person_name = document.querySelector("#person h1")
const person_occupation = document.querySelector("#person h2")
const profile_description = document.querySelector('#profile-description')
const profile_image = document.querySelector('#profile-information-image')
const profile_socials = document.querySelector("#profile-socials")
const principal = document.querySelector(".rightPages#comments")
const left = document.querySelector(".left#comments")
const menu = document.querySelector(".menu#comments")
var scrollPosition




function getIdClicked(id){
    const openModalButton = document.querySelector(`#open-info-${id}`);
    scrollPosition = window.scrollY;
    toggleModal(openModalButton)
  };
  
  const toggleModal = (openModalButton = null) => {
    if (openModalButton) {
      if (window.innerWidth < 1024){
        principal.style.height = "90px";
        left.style.display = "none";
        menu.style.display = "none"
      }
      person_name.innerHTML = openModalButton.getAttribute('profile-name')
      person_occupation.innerHTML = openModalButton.getAttribute('occupation')
      profile_description.innerHTML = openModalButton.getAttribute('description')
      if (openModalButton.getAttribute('photo')){
        profile_image.src = openModalButton.getAttribute('photo')
      }
      else {
        profile_image.src = "static/assets/no-photo.png"
      }
      const socials = openModalButton.getAttribute("socials")
      if (socials === '') {
        profile_socials.innerHTML='Este perfil não possui redes sociais'
      } else {
        var socialsArray = socials.split(',').map(function(item){
          return item.trim();
        }) 
        var organized_socials = []
        var icon, identification, is_link;
        for (let i = 0; i < socialsArray.length; i += 3) {
          identification = socialsArray[i];
          icon = socialsArray[i + 1];
          is_link = socialsArray[i + 2]
          is_link = (is_link === "True");
          organized_socials.push({ Icon: icon, Identification: identification, Is_link: is_link });
        }
        profile_socials.innerHTML=''
        organized_socials.forEach(function(item){
          var a = document.createElement('a')
          var p = document.createElement('p')
          var div = document.createElement('div')
          if(item.Is_link === true){
            a.href=`${item.Identification}`
            a.innerHTML=`<ion-icon name="${item.Icon}"</ion-icon>`;
            a.target = '_blank'
            profile_socials.appendChild(a)
          } else {
            a.innerHTML=`<ion-icon name="${item.Icon}"><p>${item.Identification}</p></ion-icon>`;
            p.innerHTML=`${item.Identification}`
            div.classList.add("profile-not-link")
            div.appendChild(a)
            div.appendChild(p)
            profile_socials.appendChild(div)
          }
        })
      }
    } else {
      principal.style.height = "";
      left.style.display = "flex";
      menu.style.display = "flex"
    }
    [info, fade].forEach((el)=> el.classList.toggle("hide"))
    window.scrollTo(0, scrollPosition);
  }
  
  [closeModalButton, fade].forEach((el) => {
    el.addEventListener("click", () => toggleModal());
  });