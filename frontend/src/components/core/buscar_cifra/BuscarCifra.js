import React from 'react'
import BotaoBuscar from './BotaoBuscar'
import InputBuscar from './InputBuscar'

const BuscarCifra = () => {
    return (
        <>
            <br />
            <br />
            <br />
            <br />
            <br />
            {/* Buscar Cifra start */}
            <form action="" method="get">
                <div className="whole-wrap">
                    <div className="container box_1170">
                        <div className="section-top-border">
                            <div className="row">
                                <InputBuscar />
                                <BotaoBuscar />
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </>

    )
}

export default BuscarCifra