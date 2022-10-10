import React from 'react'

const BotaoBuscar = () => {
    return (
        <div className="col-lg-4 col-md-4">
            <div className="button-group-area">
                <button
                    type="submit"
                    className="genric-btn primary radius"
                    id="btn_buscar"
                    name="btn_buscar_n"
                >
                    <i className="fa fa-search" aria-hidden="true" />
                    Buscar
                </button>
            </div>
        </div>

    )
}

export default BotaoBuscar