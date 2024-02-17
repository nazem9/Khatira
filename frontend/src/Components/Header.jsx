import React, { useEffect } from 'react'
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import {useNavigate  } from 'react-router-dom';
import { useAuth } from './AuthContext';
  
const Header = () => {

  const navigate = useNavigate()
const {isLogged, username,login, logout,checkUser}= useAuth();
  const handleHistory = (route) =>{
    switch(route){
      case 'home': navigate('/');break;
      case 'login':navigate('/login');break;
      case 'logout':logout();navigate('/');break;
    }
  }
  useEffect(()=>{
    checkUser()
  },[isLogged])
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1, }}>
          Khatira
        </Typography>
        <Button color="inherit" onClick={() => handleHistory('home')}>Home</Button>
        {!isLogged? <Button color="inherit" onClick={() => handleHistory('login')}>Login</Button>:
        <Button color="inherit" onClick={() => handleHistory('logout')}>Log out {username}</Button>}
        <Button color="inherit">Contact</Button>
      </Toolbar>
    </AppBar>
  )
}

export default Header