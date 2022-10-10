import React from 'react'
import feedback_user from '../../../assets/img/testmonial/testimonial1.png'

const SingleFeedback = () => {
    return (
        <div className="row d-flex justify-content-center">
            <div className="col-lg-10 col-md-9">
                <div className="h1-testimonial-active">
                    {/* Feedback */}
                    <div className="single-testimonial text-center">
                        <div className="testimonial-caption ">
                            <div className="testimonial-top-cap">
                                <p>
                                    Somos em 5 no misniterio de louvor e fazer parte do WCifras nos
                                    possibilitou organizar com facilidade a escolha e sequência de
                                    musicas para cada culto, com ordem e planejamento para as
                                    atividades da igreja.{" "}
                                </p>
                            </div>
                            {/* Usuario */}
                            <div className="testimonial-founder d-flex align-items-center justify-content-center">
                                <div className="founder-img">
                                    <img
                                        src={feedback_user}
                                        alt=""
                                    />
                                </div>
                                <div className="founder-text">
                                    <span>Janaiana Monsanto</span>
                                    <p>Igreja Batista Avivamento</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    )
}

export default SingleFeedback