import React from 'react'
import './home.css'
import { Link } from 'react-router-dom'
import { useEffect, useState } from 'react';
import axios from 'axios';
import { Tecnico } from '../../components/Cliente.js'
/*Muestro Tecnico*/
const Home = () => {

  const [tecnicos, setTecnico] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/tecnico')
      .then(res => {
        const {data} = res;
        setTecnico((prevTecnico)=>prevTecnico.concat(data));
      })
  }, []);

  if(tecnicos.length >= 1) return <h1>Loading...</h1>;

  return (
    <div>
      <Link to='/register'>Registrarse</Link>
      {tecnicos.map(tecnico => <Tecnico key={tecnico.id} {...tecnico} />)} 
    </div>
  )
}

export default Home