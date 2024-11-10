window.onload = function() {
    const cardDetails = JSON.parse(localStorage.getItem('virtualCard'));

    if (cardDetails) {
        document.getElementById('card-name').innerText = cardDetails.cardName;
        document.getElementById('card-number').innerText = cardDetails.cardNumber;
        document.getElementById('expiration-date').innerText = cardDetails.expirationDate;
        document.getElementById('cvv').innerText = cardDetails.cvv;
    } else {
        alert("No card found. Please create a card first.");
        window.location.href = "card-creation.html";
    }
};