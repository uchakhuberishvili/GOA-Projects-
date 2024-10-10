let correctCount = localStorage.getItem('correctCount') ? parseInt(localStorage.getItem('correctCount')) : 0;
const score = document.getElementById('score');

// Update score display
function updateScore() {
    score.textContent = `Your Score: ${correctCount}`;
}

// Check the answer and move to the next page
function checkAnswer(button, isCorrect, nextPage) {
    if (isCorrect) {
        button.classList.add('correct');
        correctCount++;
        localStorage.setItem('correctCount', correctCount); // Save the score
        updateScore();
    } else {
        button.classList.add('incorrect');
    }

    setTimeout(() => {
        button.classList.remove('correct', 'incorrect');
        location.href = nextPage; // Move to the next page
    }, 1000);
}

// Update score display when the page loads
updateScore();
