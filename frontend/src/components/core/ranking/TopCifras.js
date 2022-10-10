import React from 'react'

const TopCifras = () => {
    return (
        <>
            {/* Top cifras */}
            <div className="col-lg-5">
                <div className="section-top-border">
                    <div className="row d-flex justify-content-center">
                        <div className="col-lg-5  col-md-8 pr-0">
                            <div className="section-tittle text-center">
                                <h2>Top Canções</h2>
                            </div>
                        </div>
                    </div>
                    <div className="media post_item" style={{ backgroundColor: "#fcfbfd" }}>
                        <h1>1º</h1>
                        {/*<img src="../static/img/post/post_1.png" alt="post" style="margin-left: 5px">*/}
                        <div className="media-body" style={{ marginLeft: 5 }}>
                            <a href="#">
                                <h5> Lugar Secreto</h5>
                            </a>
                            <p style={{ marginTop: "-10px" }}> Gabriela Rocha</p>
                        </div>
                    </div>
                    <div className="media post_item" style={{ backgroundColor: "#fcfbfd" }}>
                        <div className="media-body" style={{ marginLeft: 5, marginTop: 10 }}>
                            <a href="#">
                                <p>
                                    {" "}
                                    Ver mais <i className="fa fa-arrow-right" aria-hidden="true" />
                                </p>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </>

    )
}

export default TopCifras