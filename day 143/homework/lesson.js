const images = document.querySelectorAll(".slider img");
let currentIndex = 0;

function showImage(index) {
  images.forEach((img, i) => {
    img.style.display = i === index ? "block" : "none";
  });
}

document.getElementById("next").addEventListener("click", function() {
  currentIndex = (currentIndex + 1) % images.length;
  showImage(currentIndex);
});

document.getElementById("prev").addEventListener("click", function() {
  currentIndex = (currentIndex - 1 + images.length) % images.length;
  showImage(currentIndex);
});

showImage(currentIndex);
