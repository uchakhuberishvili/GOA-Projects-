import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import WelcomeMessage from './components/WelcomeMessage';
import Button from './components/Button';
import UserProfile from './components/UserProfile';

function App() {
  return (
    <div>
      <Header />
      <WelcomeMessage />
      <Button />
      <UserProfile />
      <Footer />
    </div>
  );
}

// export default App;


function Header() {
    return <header><h1>Welcome to My React App</h1></header>;
  }
  
//   export default Header;

  function WelcomeMessage() {
    return <p>Welcome to the application! Enjoy your stay.</p>;
  }
  
//   export default WelcomeMessage;

  function Button() {
    return <button onClick={() => alert('Button clicked!')}>Click me</button>;
  }
  
//   export default Button;

  function UserProfile() {
    const user = { name: 'John Doe', age: 28 };
  
    return (
      <div>
        <h2>User Profile</h2>
        <p>Name: {user.name}</p>
        <p>Age: {user.age}</p>
      </div>
    );
  }
  
  export default UserProfile;
  