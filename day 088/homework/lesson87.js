let scorePlayer = 0;
let scoreComputer = 0;

function playRound(playerChoice) {
    const choices = ['rock', 'paper', 'scissors'];
    const computerChoice = choices[Math.floor(Math.random() * choices.length)];
    
    const result = determineWinner(playerChoice, computerChoice);
    if (result === 'Player wins!') {
        scorePlayer++;
    } else if (result === 'Computer wins!') {
        scoreComputer++;
    }

    document.getElementById('playerChoice').textContent = `Player choice: ${playerChoice}`;
    document.getElementById('computerChoice').textContent = `Computer choice: ${computerChoice}`;
    document.getElementById('result').textContent = result;
    document.getElementById('score').textContent = `Score: Player - ${scorePlayer} | Computer - ${scoreComputer}`;
}

function determineWinner(playerChoice, computerChoice) {
    if (playerChoice === computerChoice) {
        return 'It\'s a tie!';
    }

    if (
        (playerChoice === 'rock' && computerChoice === 'scissors') ||
        (playerChoice === 'paper' && computerChoice === 'rock') ||
        (playerChoice === 'scissors' && computerChoice === 'paper')
    ) {
        return 'Player wins!';
    } else {
        return 'Computer wins!';
    }
}

function resetGame() {
    scorePlayer = 0;
    scoreComputer = 0;
    document.getElementById('playerChoice').textContent = 'Player choice: -';
    document.getElementById('computerChoice').textContent = 'Computer choice: -';
    document.getElementById('result').textContent = '';
    document.getElementById('score').textContent = 'Score: Player - 0 | Computer - 0';
}
