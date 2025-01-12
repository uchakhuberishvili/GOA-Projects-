document.getElementById('addMoneyBtn').addEventListener('click', function() {
    const amount = parseFloat(document.getElementById('depositAmount').value);
    if (!isNaN(amount) && amount > 0) {
        let balance = document.getElementById('balance');
        let currentBalance = parseFloat(balance.textContent.replace(/[^0-9.-]+/g, ""));
        let newBalance = currentBalance + amount;
        balance.textContent = `$${newBalance.toFixed(2)}`;

        let transactions = document.getElementById('transactions');
        let newTransaction = document.createElement('li');
        newTransaction.textContent = `Deposit - +$${amount.toFixed(2)}`;
        transactions.prepend(newTransaction);
        document.getElementById('depositAmount').value = '';
    } else {
        alert('Please enter a valid amount.');
    }
});

document.getElementById('sendMoneyBtn').addEventListener('click', function() {
    const recipientName = document.getElementById('recipientName').value.trim();
    const sendAmount = parseFloat(document.getElementById('sendAmount').value);
    let balance = document.getElementById('balance');
    let currentBalance = parseFloat(balance.textContent.replace(/[^0-9.-]+/g, ""));

    if (recipientName === '') {
        alert('Please enter the recipient\'s name.');
        return;
    }

    if (isNaN(sendAmount) || sendAmount <= 0) {
        alert('Please enter a valid amount to send.');
        return;
    }

    if (sendAmount > currentBalance) {
        alert('Insufficient funds.');
        return;
    }

    let newBalance = currentBalance - sendAmount;
    balance.textContent = `$${newBalance.toFixed(2)}`;

    let transactions = document.getElementById('transactions');
    let newTransaction = document.createElement('li');
    newTransaction.textContent = `Sent to ${recipientName} - -$${sendAmount.toFixed(2)}`;
    transactions.prepend(newTransaction);

    document.getElementById('recipientName').value = '';
    document.getElementById('sendAmount').value = '';
});
