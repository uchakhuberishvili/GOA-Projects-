const jokes = [
    "Why don't skeletons fight each other? They don't have the guts.",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "I told my computer I needed a break, and it froze."
  ];
  
  function getRandomJoke() {
    const randomIndex = Math.floor(Math.random() * jokes.length);
    console.log(jokes[randomIndex]);
  }
  
  getRandomJoke();
  