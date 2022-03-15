import React from 'react';
import Navbar from '../components/navbar/Navbar.jsx'

const Layout = (props) => (
    <div>
        <Navbar />
        {props.children}
    </div>
)

export default Layout;