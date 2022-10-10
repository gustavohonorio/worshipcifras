import React from 'react'
import card1 from '../../../assets/img/card_destaque/card1.jpg'
import card2 from '../../../assets/img/card_destaque/card2.jpg'
import card3 from '../../../assets/img/card_destaque/card3.jpg'

const CardItem = () => {
    return (
        <>
            <div className="carousel-item active">
                <a href="#" target="_blank">
                    <div className="card h-100">
                        <img className="card-img-top" src={card1} alt="Card image cap" />
                        <div className="card-body">
                            <h5 className="card-title">Titulo do card</h5>
                            <p className="card-text">Descricao do card</p>
                        </div>
                    </div>
                </a>
            </div>
            <div className="carousel-item">
                <a href="#" target="_blank">
                    <div className="card h-100">
                        <img className="card-img-top" src={card2} alt="Card image cap" />
                        <div className="card-body">
                            <h5 className="card-title">Titulo do card</h5>
                            <p className="card-text">Descricao do card</p>
                        </div>
                    </div>
                </a>
            </div>
            <div className="carousel-item active">
                <a href="#" target="_blank">
                    <div className="card h-100">
                        <img className="card-img-top" src={card3} alt="Card image cap" />
                        <div className="card-body">
                            <h5 className="card-title">Titulo do card</h5>
                            <p className="card-text">Descricao do card</p>
                        </div>
                    </div>
                </a>
            </div>
        </>

    )
}

export default CardItem