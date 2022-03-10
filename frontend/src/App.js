/* react hooks */
import React from 'react'
import { useEffect, useState } from 'react';
import axios from 'axios';
/*import { Cliente } from './components/Cliente.js';*/
import Register from './components/register/Register'

import LoginUser from './containers/LoginUser/LoginUser';
/*import {Route, Routes} from 'React-router-dom'*/
/* npm install React-router-dom*/

function App() {

 
  const [clientes, setCliente] = useState([]);


  useEffect(() => {
    
    axios.get('http://127.0.0.1:8000/cliente') /* Llamar a los clientes*/
      .then(res => {
        const {data} = res;
        setCliente((prevCliente)=>prevCliente.concat(data));

      })
    
  }, []);

  if(clientes.length === 0) return <h1>Loading...</h1>;

  return (
    <>
      <LoginUser />
    </>
    
    /*<div>
      <Routes>
        <Route path='/cliente' element={
                    <Cliente />
                } />
      </Routes>
    </div>*/
    /* {clientes.map(cliente => <Cliente key={cliente.id} {...cliente} />)}*/
  );
}



export default App;
