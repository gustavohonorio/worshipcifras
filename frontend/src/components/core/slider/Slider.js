import React from 'react'
import background_slider from '../../../assets/img/hero/h1_hero.png'
import TextoSlider from './TextoSlider'

const Slider = () => {
    return (
        <>
            {/* Slider Area Start*/}
            <div className="slider-area">
                <div className="slider-active">
                    <div
                        className="single-slider slider-height d-flex align-items-center"
                        style={{ marginTop: "-100px", backgroundImage: `url(${background_slider})`}}
                    >
                        <div className="container">
                            <TextoSlider />
                        </div>
                    </div>
                </div>
            </div>
        </>

    )
}

export default Slider