const partOne = document.querySelector('.partOne')
const partTwo = document.querySelector('.partTwo')
const partThree = document.querySelector('.partThree')
const partFour = document.querySelector('.partFour')

function hiddenElement() {       
    partOne.style.display='none'
    partTwo.style.display='none'
    partThree.style.display='none'
    partFour.style.display='none'
}

hiddenElement()

function cleanElement(element = null){
    element.textContent = ''
    element.style.display=''
}

function createBlinkAnimation(element = null){
    element.classList.add('blink-animation');
}

function typeWrite(element, delay = 75){
    const textArray = element.textContent.trim().split('');
    cleanElement(element)
    createBlinkAnimation(element)

    return new Promise((resolve)=>{
        textArray.forEach((letra, i)=> {
        setTimeout(function(){
            element.textContent += letra
            if (i===textArray.length - 1) {
                resolve()
            }
        }, delay * i)
        })
       
    setTimeout(function () {
            element.classList.remove('blink-animation');
        }, delay * textArray.length);
    })    
}

async function typeWriteSequence(){
    await typeWrite(partOne)
    await typeWrite(partTwo)
    await typeWrite(partThree)
    await typeWrite(partFour)
    setTimeout(typeWriteSequence, 5000);
    setTimeout(hiddenElement, 4800)
}
typeWriteSequence()