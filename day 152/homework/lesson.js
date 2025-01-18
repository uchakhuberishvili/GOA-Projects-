function findLongestWord(sentence) {
    const words = sentence.split(' ');
    let longestWord = '';
    words.forEach(word => {
      if (word.length > longestWord.length) {
        longestWord = word;
      }
    });
    return longestWord;
  }
