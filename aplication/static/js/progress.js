// let number = document.getElementById("number")
let number = document.querySelector('#number')
let value = number.innerHTML;
let counter= 0;
setInterval(()=> {
    if(counter == value){
        clearInterval()
    }else{
        counter += 1;
        number.innerHTML = counter + "%" 
    } 
}, 30)