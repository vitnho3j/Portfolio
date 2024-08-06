const toggle = document.getElementById("btn-dark-mode-toggle");
const themeSystem = localStorage.getItem("themeSystem") || "light";

toggle.addEventListener('click', () => {
    let oldTheme = localStorage.getItem("themeSystem") || "light";
    let newTheme = oldTheme === "light" ? "dark" : "light";

    localStorage.setItem("themeSystem", newTheme);
    defineCurrentTheme(newTheme);
});

function createElements(className, iconName) {
    const li = document.createElement('li');
    li.className = className;

    const ionIcon = document.createElement("ion-icon");
    ionIcon.setAttribute('name', iconName);

    li.appendChild(ionIcon);
    return li;
}

function defineCurrentTheme(theme) {
    const darkSvg = createElements("icon1", "moon-outline");
    const lightSvg = createElements("icon2", "sunny-outline");
    document.documentElement.setAttribute("data-theme", theme);
    toggle.textContent = ""; // Clear previous icons
    if (theme === "light") {
        toggle.appendChild(darkSvg);
    } else {
        toggle.appendChild(lightSvg);
    }
}

defineCurrentTheme(themeSystem);