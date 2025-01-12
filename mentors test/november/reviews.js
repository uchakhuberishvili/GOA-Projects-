document.getElementById('reviewForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const rating = document.getElementById('rating').value;
    const review = document.getElementById('review').value;

    if(name && rating && review) {
        const reviewsContainer = document.getElementById('reviews');
        const newReview = document.createElement('div');
        newReview.classList.add('review-card');

        newReview.innerHTML = `
            <h3>${name}</h3>
            <p><span>Rating:</span> ${rating}/5</p>
            <p>${review}</p>
        `;
        
        reviewsContainer.appendChild(newReview);

        document.getElementById('reviewForm').reset();
    }
});
