const box = document.querySelector('.box');

let positionX = 0;
let positionY = 0;
let directionX = "right";





function animateBox() {
    positionX += directionX;
    if (directionX === "right") {
        positionX ++;
        if (positionX >= 500) {
            directionX = "bottom";
        }else if (directionX === "bottom") {
            positionX ++;
            if (positionY >= 500) {
                directionX = "left";
            }
        }

    }

    box.style.left = positionX + 'px';
    box.style.top = positionY + 'px';
}

setInterval(animateBox, 20);
