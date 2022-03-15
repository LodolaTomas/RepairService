import React, { useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { login } from '../../actions/auth';
import './login.css'

const Login = ({login}) => {
  const [formData, setFormData] = useState({
    email : '',
    password : ''
  });
  
  const { email, password} = formData;

  const onChange = e => setFormData({...formData, [e.target.name] : e.target.value});

  const onSubmit = e => {
    e.preventDefault();
    login(email, password)
  }

  return (
    <div>
      <h1>Hi</h1>
      <form onSubmit ={e => onSubmit(e)}>
        <div>
          <input 
          type="email"
          placeholder='Email' 
          name='email' 
          value={email}
          onChange={e => onChange(e)}
          required
          />
          <input 
          type="password"
          placeholder='Password' 
          name='password' 
          value={password}
          onChange={e => onChange(e)}
          minLength='6'
          required
          />
        </div>
        <button type='submit'>Log in</button>
      </form>
      <p>
        <Link to='/signup'>SignUp</Link>
      </p>
      <p>
        <Link to='reset_password'>Forgot?</Link>
      </p>
    </div>
  )
}

//const mapStateToProps = state => ({
  
//})

export default connect(null, {login})(Login);