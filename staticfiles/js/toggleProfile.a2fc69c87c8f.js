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
const toggleSocial = document.querySelector("#toggle-social")
var scrollPosition

document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('.toggleButtons').forEach(button => {
      button.addEventListener('click', (event) => {
          const id = event.target.getAttribute('data-id');
          startedContactsHidden();
          getIdClicked(id);
      });
  });
});

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
  const template = document.getElementById(`template-description-${openModalButton.getAttribute('data-id')}`)
  person_name.textContent = openModalButton.getAttribute('profile-name')
  person_occupation.textContent = openModalButton.getAttribute('occupation')
  profile_description.textContent = ''
  profile_description.appendChild(template.content.cloneNode(true))
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
  for (let i = 0; i < socialsArray.length; i += 4) {
    identification = socialsArray[i];
    icon = socialsArray[i + 1];
    is_link = socialsArray[i + 2]
    is_link = (is_link === "True");
    social_name = socialsArray[i + 3]
    organized_socials.push({ Icon: icon, Identification: identification, Is_link: is_link, Name:social_name });
  }
  return organized_socials
}

function cleanProfile(){
  profile_socials.textContent=''
}

function appendProfileSocials(item = null){
  profile_socials.appendChild(item)
}

function createLink(item = null){
  var a = document.createElement('a')
  var a_text = document.createElement('a')
  var div = document.createElement('div')
  const ionIcon = document.createElement('ion-icon');
  ionIcon.setAttribute('name', item.Icon)
  a.appendChild(ionIcon)
  a.target = '_blank'
  a_text.textContent = "Clique aqui"
  a_text.target = "_blank"
  if (item.Name == "Email") {
    a.href=`mailto:${item.Identification}`
    a_text.href=`mailto:${item.Identification}`
  } else if (item.Name == "Whatsapp") {
    a.href=`https://wa.me/${item.Identification}`
    a_text.href=`https://wa.me/${item.Identification}`
  } else {
    a.href=`${item.Identification}`
    a_text.href=`${item.Identification}`
  }

  a_text.id = "social-link"
  div.appendChild(a)
  div.appendChild(a_text)
  div.classList.add("container-social-link")
  appendProfileSocials(div)
}

function appendDivChild(div, element = null){
  div.appendChild(element)
}

function createSocialNoLink(item = null){
  var a = document.createElement('a')
  var p = document.createElement('p')
  var div = document.createElement('div')
  const ionIcon = document.createElement('ion-icon')
  const p2 = document.createElement('p')
  ionIcon.setAttribute('name', item.Icon)
  p2.textContent = item.Identification
  ionIcon.appendChild(p2)
  a.appendChild(ionIcon)
  a.onclick = function() {
    if(item.Identification.length > 30) {
      openNoLinkModal(item.identification);
    }
  };
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
  profile_socials.textContent='Este perfil não possui redes sociais'
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