import React, {Fragment} from 'react'
import './register.css'
/*import { useForm } from 'react-hook-form'*/
import axios from 'axios';
import {useNavigate} from 'react-router-dom'

const Register = () => {
    /*const {register, errors, handleSubmit} = useForm();*/
    const navigate = useNavigate()

    const onSubmit = (data) => {
        /* axios.post con then espero respueta*/
        data.preventDefault()
        const { target } = data
        const newCliente = {
            cuil : target.cuil.value,
            nombre : target.nombre.value,
            apellido : target.apellido.value,
        }
        axios.post('http://127.0.0.1:8000/cliente', newCliente)
        .then(res => {
            if(res.statusText === "Created"){
                navigate("/")
            }        
        })
        .error(res => {
            console.error(res)
        }) /* Comentar esto dsp*/
    }

  return (
    <>
        <div className='register'>
        <h2>Register</h2>
            <form onSubmit={onSubmit}>
                <input type='number' placeholder="Cuil" className="form-control mb-2" name="cuil"></input>
                <input placeholder="Nombre" className="form-control mb-2" name="nombre"></input>
                <input placeholder="Apellido" className="form-control mb-2" name="apellido"></input>
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

export default Register