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
var scrollPosition



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

function selectPhoto(openModalButton = null){
  if (openModalButton.getAttribute('photo')){
    profile_image.src = openModalButton.getAttribute('photo')
  }
  else {
    profile_image.src = "static/assets/no-photo.png"
  }
}

function setAttributes(openModalButton = null){
  person_name.innerHTML = openModalButton.getAttribute('profile-name')
  person_occupation.innerHTML = openModalButton.getAttribute('occupation')
  profile_description.innerHTML = openModalButton.getAttribute('description')
}

function generateSocialsArray(socials = null){
  const socialsArray = socials.split(',').map(function(item){
    return item.trim();
  })
  return socialsArray
}

function organizeList(socialsArray = null){
  var organized_socials = []
  var icon, identification, is_link;
  for (let i = 0; i < socialsArray.length; i += 3) {
    identification = socialsArray[i];
    icon = socialsArray[i + 1];
    is_link = socialsArray[i + 2]
    is_link = (is_link === "True");
    organized_socials.push({ Icon: icon, Identification: identification, Is_link: is_link });
  }
  return organized_socials
}

function cleanProfile(){
  profile_socials.innerHTML=''
}

function appendProfileSocials(item = null){
  profile_socials.appendChild(item)
}

function createLink(item = null){
  var a = document.createElement('a')
  a.href=`${item.Identification}`
  a.innerHTML=`<ion-icon name="${item.Icon}"</ion-icon>`;
  a.target = '_blank'
  appendProfileSocials(a)
}

function appendDivChild(div, element = null){
  div.appendChild(element)
}

function createSocialNoLink(item = null){
  var a = document.createElement('a')
  var p = document.createElement('p')
  var div = document.createElement('div')
  a.innerHTML=`<ion-icon name="${item.Icon}"><p>${item.Identification}</p></ion-icon>`;
  p.innerHTML=`${item.Identification}`
  div.classList.add("profile-not-link")
  appendDivChild(div, a)
  appendDivChild(div, p)
  appendProfileSocials(div)
}

function appendSocials(organized_socials = null){
  cleanProfile()
  organized_socials.forEach(function(item){
    if(item.Is_link === true){
      createLink(item)
    } else {
      createSocialNoLink(item)
    }
  })
}

function generateOrganizedSocials(socialsArray = null){
  var organized_socials = organizeList(socialsArray)
  appendSocials(organized_socials)
}

function setNoSocials(){
  profile_socials.innerHTML='Este perfil não possui redes sociais'
}

function setSocials(openModalButton = null){
  const socials = openModalButton.getAttribute("socials")
  if (socials === '') {
    setNoSocials()
  } else {
    var socialsArray = generateSocialsArray(socials)
    generateOrganizedSocials(socialsArray)
  }
}

function getIdClicked(id){
    const openModalButton = document.querySelector(`#open-info-${id}`);
    scrollPosition = window.scrollY;
    toggleModal(openModalButton)
  };
  
  const toggleModal = (openModalButton = null) => {
    if (openModalButton) {
      if (window.innerWidth < 1024){
        hideBackground()
      }
      setAttributes(openModalButton)
      selectPhoto(openModalButton)
      setSocials(openModalButton)
    } else {
      showBackground()
    }
    [info, fade].forEach((el)=> el.classList.toggle("hide"))
    window.scrollTo(0, scrollPosition);
  }
  
  [closeModalButton, fade].forEach((el) => {
    el.addEventListener("click", () => toggleModal());
  });