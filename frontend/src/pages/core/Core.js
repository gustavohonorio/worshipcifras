import React from 'react'

// components
//import PreLoader from '../../components/core/preloader/PreLoader'
import Navbar from '../../components/core/navbar/Navbar';
import BuscarCifra from '../../components/core/buscar_cifra/BuscarCifra';
import Slider from '../../components/core/slider/Slider';
import Ranking from '../../components/core/ranking/Ranking';
import Feedback from '../../components/core/feedback/Feedback';
import Footer from '../../components/core/footer/Footer';
import CardDestaque from '../../components/core/card_destaque/CardDestaque';

const Core = () => {
    return (
        <>
            {/* <PreLoader /> */}
            <Navbar />
            <BuscarCifra />
            <main>
                <CardDestaque />
                <Slider />
                <Ranking />
                <Feedback />
            </main>
            <Footer />
        </>
    )
}

export default Core