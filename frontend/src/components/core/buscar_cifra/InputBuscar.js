import React from 'react'

const InputBuscar = () => {
    return (
        <div className="col-lg-8 col-md-8">
            <div className="mt-10">
                <input
                    type="text"
                    id="buscar"
                    name="buscar_n"
                    placeholder="O que você vai tocar hoje?"                    
                    className="single-input"
                />
            </div>
        </div>

    )
}

export default InputBuscar