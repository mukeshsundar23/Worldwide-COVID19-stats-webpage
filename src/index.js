import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {Auth0Provider} from '@auth0/auth0-react';


ReactDOM.render(
  <Auth0Provider
  domain="dev-3cnyeetuvwf36hop.us.auth0.com"
  clientId="yKUEVPARb9uDLUlnN47Rbn9TxRSyzu1Z"
  redirectUri={window.location.origin}
  >
  
  <React.StrictMode>
    <App />
  </React.StrictMode>
  </Auth0Provider>,
  document.getElementById('root')
);

reportWebVitals();
