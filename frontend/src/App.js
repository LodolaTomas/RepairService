/* react hooks */
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Provider } from 'react-redux';

import store from './store.js';

import Home from './containers/home/Home.jsx'
import Login from './containers/login/Login.jsx'
import Signup from './containers/signup/Signup.jsx'
import Resetpassword from './containers/resetpassword/Resetpassword.jsx'
import Resetpasswordconfirm from './containers/resetpasswordconfirm/Resetpasswordconfirm.jsx'
import Activate from './containers/activate/Activate.jsx'
import Layout from './hocs/Layout';

function App(){
  return(
    <div>
      <Provider store={store}>
          <Layout>
              <Routes>
                  <Route path='/' element={<Home />} />
                  <Route path='/login' element={<Login />} />
                  <Route path='/signup' element={<Signup />} />
                  <Route path='/reset_password' element={<Resetpassword />} />
                  <Route exact path='/password/reset/confirm/:uid/:token' element={<Resetpasswordconfirm />} />
                  <Route path='/activate/:uid/:token' element={<Activate />} />
              </Routes>
          </Layout>
      </Provider>


    </div>
  )
}

export default App;
