import React from 'react'
import BotaoEntrarSair from './BotaoEntrarSair'
import Logo from './Logo'
import MainMenu from './MainMenu'
import MobileMenu from './MobileMenu'

const Navbar = () => {
    return (
        <div className="header-area header-transparrent ">
            <div className="main-header header-sticky">
                <div className="container">
                    <div className="row align-items-center">
                        <Logo />
                        <MainMenu />
                        <BotaoEntrarSair />
                        <MobileMenu />
                    </div>
                </div>
            </div>
        </div>

    )
}

export default Navbar