document.addEventListener('DOMContentLoaded', () => {
    const prev = document.getElementById('prev');
    const next = document.getElementById('next');
    const image = document.getElementById('image');

    let currentImage = 'goa';

    function updateImage(imageName) {
        image.src = `${imageName}.jpg`;
    }

    prev.addEventListener('click', () => {
        if (currentImage !== 'goa') {
            currentImage = 'goa';
            updateImage(currentImage);
        }
    });

    next.addEventListener('click', () => {
        if (currentImage !== 'Novatori') {
            currentImage = 'Novatori';
            updateImage(currentImage);
        }
    });
});
// ქოდვარსები ავტვირთე CodeWars ფოლდერში სულ მაღლა სახელად "day 088 codewars"