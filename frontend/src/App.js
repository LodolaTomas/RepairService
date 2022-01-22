import {useEffect, useState} from 'react';
/* react hooks */
import { Cliente} from './components/Cliente';

function App() {

  const [clientes, setcliente] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:8000/cliente')
      .then(res => res.json())
      .then(data => setcliente(clientes => clientes.concat(data)))
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        {clientes.map(cliente => (
          <Cliente key={cliente.id} {...cliente} />
        ))}
      </header>
    </div>
  );
}



export default App;
