import logo from './logo.svg';
import './App.css';
import LoginButton from './components/loginbutton';
import LogoutButton from './components/logoutbutton';
import UserProfile from './components/userprofile';

function App() {
  return (
    <div className="App">
      <LoginButton/>
      <LogoutButton/>
      <p>The Users information is below!</p>
      <UserProfile/>
    </div>
  );
}

export default App;
