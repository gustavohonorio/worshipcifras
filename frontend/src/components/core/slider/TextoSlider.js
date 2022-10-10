import React from 'react'

const TextoSlider = () => {
    return (
        <div className="row d-flex align-items-center">
            <div className="col-lg-7 col-md-9 ">
                <div className="hero__caption">
                    <h1 data-animation="fadeInLeft" data-delay=".4s">
                        Worship Cifras
                    </h1>
                    <p data-animation="fadeInLeft" data-delay=".6s">
                        Busque a excelência para o seu momento de adoração. O WCifras foi
                        pensado exclusivamente para você e para o seu ministério. Crie uma conta
                        e aproveite os recursos que irá auxiliar na sua performance ao vivo e no
                        secreto. E o melhor, é grátis.
                    </p>
                    {/* Botão entrar */}
                    <div className="hero__btn" data-animation="fadeInLeft" data-delay=".8s">
                        <a href="{% url 'login' %}" className="btn hero-btn">
                            Entrar
                        </a>
                    </div>
                </div>
            </div>
            <div className="col-lg-5">
                <div
                    className="hero__img d-none d-lg-block"
                    data-animation="fadeInRight"
                    data-delay="1s"
                >
                    <img src="" alt="" />
                    {/*../static/img/hero/hero_right.png */}
                </div>
            </div>
        </div>

    )
}

export default TextoSlider