document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os elementos com a classe 'water_wave'
    const waterWaves = document.querySelectorAll('.water_wave');

    // Itera sobre cada elemento e define o estilo baseado no data-percentage
    waterWaves.forEach(function(waterWave) {
        const percentage = waterWave.getAttribute('data-percentage');
        waterWave.style.setProperty('--percentageNumber', `${percentage}%`);
    });
});