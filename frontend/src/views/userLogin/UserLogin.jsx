import React from 'react'
import './userLogin.css'
import { Link } from 'react-router-dom'
import Login from '../../components/login/Login'
import Register from '../../components/register/Register'


const UserLogin = () => {
  return (
    <>
      <Link to='/'>Home</Link>
        <div>
            <div>
                <Login />
            </div>
            <div>
                <Register />
            </div>
        </div>
    </>
  )
}

export default UserLogin