import React from 'react'
import SingleFeedback from './SingleFeedback'
import TitleSection from './TitleSection'

const Feedback = () => {
    return (
        <>
            {/* Testemunhos dos Clientes */}
            <div className="testimonial-area">
                <div className="container">
                    <div className="testimonial-main">
                        <TitleSection />
                        <SingleFeedback />
                    </div>
                </div>
            </div>
        </>

    )
}

export default Feedback