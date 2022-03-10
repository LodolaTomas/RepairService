import React from 'react'
import Register from '../../components/register/Register'
import Login from '../../components/login/Login'
import './loginUser.css'

const LoginUser = () => {
  return (
    <>
        <div className="contenedor">
            <div className="contenedor-izq"><Login /></div>
            <div className="contenedor-der"><Register /></div>
        </div>
           
    </>
  )
}

export default LoginUser