let number = document.querySelector('#number')
let value = number.textContent;
let counter= 0;
setInterval(()=> {
    if(counter == value){
        clearInterval()
    }else{
        counter += 1;
        number.textContent = counter + "%" 
    } 
}, 30)