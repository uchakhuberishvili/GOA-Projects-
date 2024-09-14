const form = document.getElementById('forms');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const dateInput = document.getElementById('date').value;
    const monthInput = document.getElementById('month').value;
    const yearInput = document.getElementById('year').value;

    if (!dateInput || !monthInput || !yearInput) {
        alert("შეავსე ველები.");
        return;
    }

    const date = new Date(dateInput);
    const month = new Date(monthInput + '-01');
    const year = parseInt(yearInput, 10);

    const currentDate = new Date();
    const age = currentDate.getFullYear() - year;

    alert(`შენ ხარ ${age} წლის.`);
});

const inputs = form.querySelectorAll('input[type="date"], input[type="month"], input[type="number"]');

inputs.forEach((input) => {
    input.addEventListener('input', () => {
    });
});
