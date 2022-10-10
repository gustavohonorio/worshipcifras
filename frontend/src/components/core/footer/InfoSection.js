import React from 'react'

import logo_footer from '../../../assets/img/logo/logo2_footer.png'

const InfoSection = () => {
    return (
        <div className="col-lg-3 col-md-4 col-sm-8">
            <div className="single-footer-caption mb-50">
                <div className="single-footer-caption mb-30">
                    {/* logo */}
                    <div className="footer-logo">
                        <a href="#">
                            <img src={logo_footer} alt="" />
                        </a>
                    </div>
                    <div className="footer-tittle">
                        <div className="footer-pera">
                            {/*<p class="info1">CNPJ 00123456/0001-23<br>São Carlos SP - Brasil</p>*/}
                            <p className="info1">São Carlos SP - Brasil</p>
                            <p className="info2">contato@worshipcifras.com.br</p>
                        </div>
                    </div>
                    <div className="footer-social">
                        <a href="https://www.facebook.com/worshipcifras" target="_blank">
                            <i className="fab fa-facebook-f" />
                        </a>
                        <a href="https://www.instagram.com/worshipcifras/" target="_blank">
                            <i className="fab fa-instagram" />
                        </a>
                        <a href="https://twitter.com/CifrasWorship" target="_blank">
                            <i className="fab fa-twitter" />
                        </a>
                        {/*<a href="#"><i class="fab fa-linkedin"></i></a>*/}
                    </div>
                </div>
            </div>
        </div>

    )
}

export default InfoSection