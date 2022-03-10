import React from 'react'
import "./login.css"

const Login = () => {
  return (
    <>
        <div className='login'>
            <h1>Login</h1>
            <form>
                <input placeholder="Nombre" className="form-control mb-2" name="nombre"></input>
                <input placeholder="Password" type="password" className="form-control mb-2" name="password"></input>
                <div className='btn'>
                    <button type="submit" className="btn-primary">
                        Enviar
                    </button>
                </div>
                
            </form>    
        </div>
    </>
  )
}

export default Login