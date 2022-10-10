import React from 'react'

const MainMenu = () => {
    return (
        <div className="col-xl-8 col-lg-8 col-md-8">
            {/* Main-menu */}
            <div className="main-menu f-right d-none d-lg-block">
                {/* Menu do usuário anonimo */}
                <nav>
                    <ul id="navigation">
                        <li>
                            <a href="#">Enviar cifra</a>
                        </li>
                        <li>
                            <a href="#">Cadastrar artista</a>
                        </li>
                        <li>
                            <a href="#">Entrar</a>
                        </li>
                    </ul>
                </nav>
            </div>
        </div>

    )
}

export default MainMenu