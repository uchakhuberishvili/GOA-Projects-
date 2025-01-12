let loanAmount = 0;
let loanTerm = 0;
let loanBalance = 0;
let totalPaid = 0;
let monthlyPayment = 0;

function calculateLoanDetails() {
    if (loanAmount > 0 && loanTerm > 0) {
        monthlyPayment = (loanAmount / loanTerm).toFixed(2);
        loanBalance = loanAmount;
        updateLoanDetails();
    }
}

function updateLoanDetails() {
    document.getElementById('loan-balance').innerText = `Loan Amount: $${loanBalance.toFixed(2)}`;
    document.getElementById('monthly-payment').innerText = `Monthly Payment: $${monthlyPayment}`;
    document.getElementById('repayment-status').innerText = `Amount Paid: $${totalPaid.toFixed(2)} | Remaining Balance: $${loanBalance.toFixed(2)}`;
}

document.getElementById('loan-form').addEventListener('submit', function(event) {
    event.preventDefault();
    loanAmount = parseFloat(document.getElementById('loan-amount').value);
    loanTerm = parseInt(document.getElementById('loan-term').value);
    calculateLoanDetails();
});

document.getElementById('payment-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const paymentAmount = parseFloat(document.getElementById('payment-amount').value);

    if (paymentAmount > 0 && loanBalance > 0) {
        totalPaid += paymentAmount;
        loanBalance -= paymentAmount;
        updateLoanDetails();
        alert(`Payment of $${paymentAmount} has been made.`);
    } else {
        alert("Please enter a valid payment amount.");
    }
});
