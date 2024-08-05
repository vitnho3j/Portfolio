var textarea = document.getElementById("text-area");
var charCountSpan = document.getElementById("charCount");

textarea.addEventListener("input", function() {
    var text = textarea.value;
    var charCount = text.length;
    console.log("Contagem de caracteres no cliente:", charCount);
    charCountSpan.textContent = charCount;
    if (charCount > 1500) {
        charCountSpan.classList.add("over-limit");
    } else {
        charCountSpan.classList.remove("over-limit");
    }
});
