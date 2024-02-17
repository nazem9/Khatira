import React, {useState,useContext,useEffect} from 'react';
import axios from 'axios';
import Cookies from 'js-cookie';
const AuthContext = React.createContext();
export const useAuth = () => useContext(AuthContext); 

const AuthPorvider = ({children}) => 
{
  const [isLogged,setIslogged] = useState(false);
  const [username,setUsername] = useState()
  
  const authclient = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/auth',withCredentials: true,
    headers: {
        "Content-type": "application/json",
    },
  })

  const checkUser = ()=>{
    authclient.get("/user",{withCredentials:true}).then(res=>{
      if(res.data){
        setUsername(res.data.user.username);
        setIslogged(true)
      }else{
        setIslogged(false)
      }
    }).then().catch(err =>{
      setIslogged(false)
    })
  }

  const login = (username,password) =>{
    let res = false
    authclient.post('/login',
    {
      username: username,
      password:password,
    },{withCredentials: true}).then((response)=>{
      res = true
    }).catch(error=>{
      res =  false
    });
    return res;
  }

const logout =()=>{
  authclient.post('/logout',{},{withCredentials:true})
}
  return (
    <AuthContext.Provider value={{ isLogged,username,login,logout,checkUser }}>
    {children}
  </AuthContext.Provider>
  )
}

export default AuthPorvider;
