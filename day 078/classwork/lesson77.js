const me = {
    name: "უჩა",
    city: "მცეთა",
    age: 15,
    academy: "გოა"
}
console.log(me);

let firstParagraph = document.getElementById("first");
firstParagraph.textContent = "Changed first paragraph";
let secondParagraph = document.getElementById("second");
secondParagraph.textContent = "Changed second paragraph";

function sums(a,b){
    console.log(a + b)
}
sums(10,50)

    

function change() {
    let paragraph = document.getElementById("parag");
    paragraph.textContent = "Goa";
}

function changeText(color) {
    document.getElementById('change').style.color = color;
    document.getElementById('change').style.backgroundColor = 'purple'
}