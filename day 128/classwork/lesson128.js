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



function Header() {
    return <header><h1>Welcome to My React App</h1></header>;
  }
  

  function WelcomeMessage() {
    return <p>Welcome to the application! Enjoy your stay.</p>;
  }

  function Button() {
    return <button onClick={() => alert('Button clicked!')}>Click me</button>;
  }
  

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
  