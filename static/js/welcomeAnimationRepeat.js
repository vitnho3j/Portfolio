
function welcomeAnimationRepeat() {
    var welcome = document.getElementById('welcome');
    welcome.style.display = (welcome.style.display === 'none' || welcome.style.display === '') ? '' : 'none';
}

setInterval(welcomeAnimationRepeat, 6000)