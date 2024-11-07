let correctCount = localStorage.getItem('correctCount') ? parseInt(localStorage.getItem('correctCount')) : 0;
const score = document.getElementById('score');

function updateScore() {
    score.textContent = `Your Score: ${correctCount}`;
}


function checkAnswer(button, isCorrect, nextPage) {
    if (isCorrect) {
        button.classList.add('correct');
        correctCount++;
        localStorage.setItem('correctCount', correctCount);
        updateScore();
    } else {
        button.classList.add('incorrect');
    }

    setTimeout(() => {
        button.classList.remove('correct', 'incorrect');
        location.href = nextPage;
    }, 1000);
}

updateScore();
