import PinchZoom from 'https://unpkg.com/pinch-zoom-js@2.3.5/dist/pinch-zoom.min.js';

let isZoomedIn = false;
let currentZoom = 1;
let nextZoom = 1;
let nextZoomIndex = 1;

window.usePinchZoom = function(img, index) {
    new PinchZoom(img, {
        useMouseWheel: false, // Permitir o uso da roda do mouse para zoom
        useDoubleTap: true,  // Permitir o uso de duplo toque para zoom
        draggableUnzoomed: false, // Não permitir arrastar quando não estiver com zoom
        maxZoom: 10, // Definir o zoom máximo
        minZoom: 1, // Definir o zoom mínimo
        use2d: false,
        lockDragAxis: true,
        zoomOutFactor:true,
        tapZoomFactor: 2, // Fator de zoom ao clicar duas vezes
        onZoomStart: function(object, event) {
            img.style.transition = 'transform 0.3s ease'; // Suavizar transições
        },
        onDragUpdate:function(object, event){
            event.preventDefault();
        },
    });
    img.style.position = '';
};

function clearImgReferences(){
    isZoomedIn = false;
    currentZoom = 1;
    nextZoom = 1;
    nextZoomIndex = 1;
}

function imgAddEventListenerMouseLeave(img){
    img.addEventListener("mouseleave", () => {
        img.classList.remove("zoom-in");
        img.classList.remove("zoom-out");
        img.style.removeProperty('--x');
        img.style.removeProperty('--y');
        img.style.removeProperty('--zoom');
        clearImgReferences();
    });
}

function imgAddEventListenerMouseMove(img){
    img.addEventListener("mousemove", (e) => {
        if (isZoomedIn) {
            const size = img.getBoundingClientRect();
            const x = (e.clientX - size.left) / size.width * 100;
            const y = (e.clientY - size.top) / size.height * 100;

            img.style.setProperty('--x', x + '%');
            img.style.setProperty('--y', y + '%');
        }
    });
}

function imgAddEventListenerClick(img, index) {
    img.classList.add(`image-${index}`);
    img.addEventListener("click", (e) => {
        const size = img.getBoundingClientRect();
        const x = (e.clientX - size.left) / size.width * 100;
        const y = (e.clientY - size.top) / size.height * 100;

        const zoomLevels = [1, 2, 3, 4];
        currentZoom = parseFloat(img.style.getPropertyValue('--zoom')) || 1;
        nextZoomIndex = (zoomLevels.indexOf(currentZoom) + 1) % zoomLevels.length;
        nextZoom = zoomLevels[nextZoomIndex];

        if (nextZoom === zoomLevels[zoomLevels.length - 1]) {
            img.style.setProperty('cursor', 'zoom-out');
        } else {
            img.style.setProperty('cursor', 'zoom-in');
        }

        if (currentZoom === zoomLevels[zoomLevels.length - 1]) {
            img.classList.remove("zoom-in");
            img.classList.add("zoom-out");
            img.style.setProperty('--zoom', 1);
            isZoomedIn = false;
        } else {
            img.classList.add("zoom-in");
            img.style.setProperty('--x', x + '%');
            img.style.setProperty('--y', y + '%');
            img.style.setProperty('--zoom', nextZoom);
            isZoomedIn = true;
        }
    });
}

window.zoomToDesktopImages = function (img, index){
    imgAddEventListenerClick(img, index);
    imgAddEventListenerMouseMove(img);
    imgAddEventListenerMouseLeave(img);
}
