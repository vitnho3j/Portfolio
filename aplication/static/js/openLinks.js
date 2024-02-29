const button = document.querySelector("#open-links")

function toggleDiv() {
    var div = document.querySelector(".profile-socials");
    var computedStyle = window.getComputedStyle(div);
    if (computedStyle.display === "none") {
        div.classList.remove("animation-reverse-items");
        div.style.display = "flex";
    } else {
        div.classList.remove('animation-items');
        div.classList.add("animation-reverse-items");
        setTimeout(() => {
            div.style.display = "none";
        }, 300); 
    }
}

