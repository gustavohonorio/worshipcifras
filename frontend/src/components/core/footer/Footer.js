import React from 'react'
import FooterArea from './FooterArea'
import FooterBottom from './FooterBottom'

// images
import bg_footer from '../../../assets/img/shape/footer_bg.png'

const Footer = () => {
    return (
        <>
            {/* Footer Start*/}
            <footer>
                <div
                    className="footer-main"
                    style={{ backgroundImage: `url(${bg_footer})` }}
                >
                    <FooterArea />
                    <FooterBottom />
                </div>
            </footer>
        </>

    )
}

export default Footer