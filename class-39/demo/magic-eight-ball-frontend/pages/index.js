import { useState } from "react";
import axios from 'axios';

import MagicEigthBallGame from "../components/magic-eight-ball-game";
import LoginForm from "../components/login-form";

const baseUrl = 'http://127.0.0.1:8000';
const tokenUrl = baseUrl + '/api/token/';
const refreshToken = baseUrl + '/api/token/refresh/';



export default function Home() {

  const [token, setToken] = useState('');
  const [refreshToken, setRefreshToken] = useState('');

  async function getToken(credentials){
    const fetchedToken = await axios.post(tokenUrl, credentials);
    setToken(fetchedToken.data.access);
    setRefreshToken(fetchedToken.data.refresh);
  }

  function loginHandler(credentials){
    getToken(credentials);
  }

  // if not logged in, show the login page
  // else show magic eight ball component

  // Need to persist data?
  // localStorageToken = getFromLocalStorage()

  console.log(token);
  if (!token) return <LoginForm loginHandler={loginHandler}/>
  return(
    <MagicEigthBallGame token={token}/>
  );
}
