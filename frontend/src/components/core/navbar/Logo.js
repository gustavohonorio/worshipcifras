import React from 'react'
import logo from '../../../assets/img/logo/logo.png'

const Logo = () => {
    return (
        <>
            {/* Logo */}
            <div className="col-xl-2 col-lg-2 col-md-1">
                <div className="logo">
                    <a href="#">
                        <img src={logo} alt="" />
                    </a>
                </div>
            </div>
        </>

    )
}

export default Logo