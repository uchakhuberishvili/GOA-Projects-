function searchUser() {
    const username = document.getElementById('username').value;
    const url = `https://api.github.com/users/${username}`;

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('User not found');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('user-info').innerHTML = `
                <img src="${data.avatar_url}" alt="${data.login}" width="100">
                <h2>${data.login}</h2>
                <p>${data.bio || "No bio available"}</p>
                <p>Public Repositories: ${data.public_repos}</p>
                <a href="${data.html_url}" target="_blank">Visit Profile</a>
            `;
        })
        .catch(error => {
            document.getElementById('user-info').innerHTML = `<p>${error.message}</p>`;
        });
}
