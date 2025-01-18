function checkPasswordStrength(password) {
    if (password.length < 6) {
      return "Weak";
    } else if (password.length >= 6 && password.length <= 10) {
      return "Moderate";
    } else {
      return "Strong";
    }
  }
