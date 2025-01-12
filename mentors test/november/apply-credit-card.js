document.getElementById('payment-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const cardName = document.getElementById('card-name').value;
    const cardNumber = document.getElementById('card-number').value;
    const expirationDate = document.getElementById('expiration-date').value;
    const cvv = document.getElementById('cvv').value;

    if (!cardName || !cardNumber || !expirationDate || !cvv) {
        alert("Please fill out all fields correctly.");
        return;
    }

    alert(`Payment Successful!\n\nCardholder: ${cardName}\nAmount: $500\nTransaction Successful!`);
    document.getElementById('payment-form').reset();
});