const toggle = document.getElementById("btn-dark-mode-toggle")
const themeSystem = localStorage.getItem("themeSystem") || "light"

toggle.addEventListener('click', ()=> {
    let oldTheme = localStorage.getItem("themeSystem") || "light"
    let newTheme = oldTheme == "light" ? "dark" : "light"

    localStorage.setItem("themeSystem", newTheme)
    defineCurrentTheme(newTheme)
})

function defineCurrentTheme(theme){
    const darkSvg = '<li class="icon1"><ion-icon name="moon-outline"></ion-icon></li>'
    const lightSvg = '<li class="icon2"><ion-icon name="sunny-outline"></ion-icon></li>'
    document.documentElement.setAttribute("data-theme", theme)
    if(theme == "light"){
        toggle.innerHTML = darkSvg
    } else {
        toggle.innerHTML = lightSvg
    }
}

defineCurrentTheme(themeSystem)