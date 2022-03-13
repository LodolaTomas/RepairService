/* react hooks */
import React from 'react'
import UserLogin from './views/userLogin/UserLogin.jsx'
import Home from './views/home/Home.jsx'
import {Route, Routes} from 'react-router-dom'
/* npm install React-router-dom*/

function App() {

  return (

    <div>
      <Routes>
        <Route path='/register' element={
                    <UserLogin />
                } />
        <Route path='/' element={
                    <Home />
                } />
      </Routes>
    </div>
  );
}

export default App;
