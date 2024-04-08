var textarea = document.getElementById("text-area");
var charCountSpan = document.getElementById("charCount");

textarea.addEventListener("input", function() {
    // var trimmedText = textarea.value.trim();
    // console.log("Contagem de caracteres no cliente:", trimmedText.length);
    // charCountSpan.textContent = trimmedText.length;
    // if (trimmedText.length > 1500) {
    // charCountSpan.classList.add("over-limit");
    // } else {
    // charCountSpan.classList.remove("over-limit");
    // }
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
