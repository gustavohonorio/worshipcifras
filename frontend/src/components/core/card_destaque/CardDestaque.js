import React from 'react'
import CardItem from './CardItem'

const CardDestaque = () => {
    return (
        <div className="container">
            <div
                id="carouselExampleControls"
                className="carousel slide"
                data-bs-interval="false"
                data-bs-ride="carousel"
            >
                <div className="carousel-inner">
                    <CardItem />
                </div>
                <a
                    className="carousel-control-prev"
                    href="#carouselExampleControls"
                    role="button"
                    data-slide="prev"
                >
                    <span className="carousel-control-prev-icon" aria-hidden="true" />
                    <span className="sr-only">Previous</span>
                </a>
                <a
                    className="carousel-control-next"
                    href="#carouselExampleControls"
                    role="button"
                    data-slide="next"
                >
                    <span className="carousel-control-next-icon" aria-hidden="true" />
                    <span className="sr-only">Next</span>
                </a>
            </div>
        </div>

    )
}

export default CardDestaque