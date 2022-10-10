import React from 'react'
import bg_img from '../../../assets/img/team/have.jpg'
import BotaoDestaque from './BotaoDestaque'
import TituloDestaque from './TituloDestaque'

const BannerDestaque = () => {
    return (
        <>
            {/* Banner Destaque Start */}
            <div className="have-project">
                <div className="container">
                    <div className="haveAproject" style={{ backgroundImage: `url(${bg_img})` }}>
                        <div className="row d-flex align-items-center">
                            <TituloDestaque />
                            <BotaoDestaque />
                        </div>
                    </div>
                </div>
            </div>
        </>

    )
}

export default BannerDestaque