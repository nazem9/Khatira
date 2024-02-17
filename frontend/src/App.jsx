import Login from './Pages/Login'
import Header from './Components/Header'
import Footer from './Components/Footer.jsx'
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';
import axios from 'axios';
import Home from './Pages/Home.jsx';
import React,{ useState,useEffect, } from 'react';
import AuthPorvider from './Components/AuthContext.jsx';

function App() {
  // default axios parameters
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;




  return (

    <Router>
      <AuthPorvider>
        <Header />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/login' element={<Login />}>
          </Route>
          
      </Routes>
</AuthPorvider>
    </Router>
  )
}

export default App
