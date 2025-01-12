document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const users = JSON.parse(localStorage.getItem('users')) || [];

    const user = users.find(u => u.email === email && u.password === password);

    if (user) {
        if (user.role === 'admin') {
            window.location.href = 'adminPanel.html';
        } else {
            window.location.href = 'home.html';
        }
    } else {
        alert('No account found or incorrect credentials!');
    }
});
