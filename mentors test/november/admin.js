window.onload = function () {
    let users = JSON.parse(localStorage.getItem('users')) || [];

    const usersContainer = document.getElementById('usersList');
    usersContainer.innerHTML = '';

    if (users.length === 0) {
        usersContainer.innerHTML = '<p>No users registered yet.</p>';
    } else {
        users.forEach(user => {
            let userDiv = document.createElement('div');
            userDiv.classList.add('user');
            userDiv.innerHTML = `
                <p>Name: ${user.name}</p>
                <p>Email: ${user.email}</p>
                <p>Role: ${user.role}</p>
                <button class="deleteUser" data-email="${user.email}">Delete</button>
            `;
            usersContainer.appendChild(userDiv);
        });

        const deleteButtons = document.querySelectorAll('.deleteUser');
        deleteButtons.forEach(button => {
            button.addEventListener('click', function () {
                const emailToDelete = button.getAttribute('data-email');
                deleteUser(emailToDelete);
            });
        });
    }
};

function deleteUser(email) {
    let users = JSON.parse(localStorage.getItem('users')) || [];
    users = users.filter(user => user.email !== email);
    localStorage.setItem('users', JSON.stringify(users));

    alert('User deleted successfully!');
    window.location.reload();
}
