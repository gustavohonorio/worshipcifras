import React from 'react'

const HelpSection = () => {
    return (
        <div className="col-lg-2 col-md-4 col-sm-7">
            <div className="single-footer-caption mb-50">
                <div className="footer-tittle">
                    <h4>Ajuda</h4>
                    <ul>
                        {/*<li><a href="#">FAQ</a></li>*/}
                        <li>
                            <a
                                href="#"
                                download="Política de Privacidade WorshipCifras 012022.pdf"
                            >
                                Política de Privacidade
                            </a>
                        </li>
                        <li>
                            <a href="#" download="Termos e Condições WorshipCifras 012022.pdf">
                                Termos e condições
                            </a>
                        </li>
                        {/*<li><a href="#">Trabalhe conosco</a></li>*/}
                        <li>
                            <a href="#">Reportar um bug</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

    )
}

export default HelpSection