/* react hooks */
import { useEffect, useState } from 'react';
import axios from 'axios';
import { Cliente } from './components/Cliente.js';

function App() {

  /* 
  El useState se confoma de dos cosas diferentes, por un lado tendriamos una forma  de actualizar el estado ,
  que lo tendriamos en la posicion 1 y por otro lado tendriamos el valor.
  const contador =  useState(0); devuelve un array de dos posiciones, la primera es el valor y la segunda es la funcion
  const contadorValue =  contador[0]; el valor del estado
  const updateContador =  contador[1]; devuelve un metodo que al ejecutar podemos actualizar el valor del estado
  */
  const [clientes, setCliente] = useState([]);

  /* useEffect es un hook que se ejecuta cada vez q se renderiza nuestro componente */
  useEffect(() => {
    /* metodo que nos permite recuperar datos de internet a partir de una direccion  */
    /* fetch es una peticion y esto ocurre de manera asyncrona osea que nuestra app no va a esperar que la peticion finalize */
    axios.get('http://127.0.0.1:8000/cliente')
      .then(res => {
        const {data} = res;
        setCliente((prevCliente)=>prevCliente.concat(data));
      })
    /* 
    setcliente(clientes.concat(cliente)) this is not the same of
    this

    setcliente((clientes)=>{
      return clientes.concat(cliente)
    }) 
    or this
    setcliente(clientes=>clientes.contact(cliente))
    */
  }, []);

  if(clientes.length === 0) return <h1>Loading...</h1>;

  return (
    <>
      {clientes.map(cliente => <Cliente key={cliente.id} {...cliente} />)}
    </>
  );
}



export default App;
