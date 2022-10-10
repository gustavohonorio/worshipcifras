import React from 'react'
import HelpSection from './HelpSection'
import InfoSection from './InfoSection'
import NewsSection from './NewsSection'
import PagesSection from './PagesSection'

const FooterArea = () => {
    return (
        <>
            <div className="footer-area footer-padding">
                <div className="container">
                    <div className="row d-flex justify-content-between">
                        <InfoSection />
                        <PagesSection />
                        <HelpSection />
                        <NewsSection />
                    </div>
                </div>
            </div>
        </>
    )
}

export default FooterArea