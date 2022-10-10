import React from 'react'

import { Helmet } from "react-helmet";

const JsImport = () => {
  return (
    <Helmet>
        {/* USANDO ESTA LIB HELMET PARA IMPORTAR OS JS INTERNOS DO APP */}
        
        {/* All JS Custom Plugins Link Here */}
        <script type="text/jsx" src="./assets/js/vendor/modernizr-3.5.0.min.js"></script>
        {/* Jquery, Popper, Bootstrap */}
        <script type="text/jsx" src="./assets/js/vendor/jquery-1.12.4.min.js"></script>
        <script type="text/jsx" src="./assets/js/popper.min.js"></script>
        <script type="text/jsx" src="./assets/js/bootstrap.min.js"></script>
        {/* Jquery Mobile Menu */}
        <script type="text/jsx" src="./assets/js/jquery.slicknav.min.js"></script>

        {/* Jquery Slick , Owl-Carousel Plugins */}
        <script type="text/jsx" src="./assets/js/owl.carousel.min.js"></script>
        <script type="text/jsx" src="./assets/js/slick.min.js"></script>
        {/* Date Picker */}
        <script type="text/jsx" src="./assets/js/gijgo.min.js"></script>
        {/* One Page, Animated-HeadLin */}
        <script type="text/jsx" src="./assets/js/wow.min.js"></script>
        <script type="text/jsx" src="./assets/js/animated.headline.js"></script>
        <script type="text/jsx" src="./assets/js/jquery.magnific-popup.js"></script>

        {/* Scrollup, nice-select, sticky */}
        <script type="text/jsx" src="./assets/js/jquery.scrollUp.min.js"></script>
        <script type="text/jsx" src="./assets/js/jquery.nice-select.min.js"></script>
        <script type="text/jsx" src="./assets/js/jquery.sticky.js"></script>

        {/* contact js */}
        <script type="text/jsx" src="./assets/js/contact.js"></script>
        <script type="text/jsx" src="./assets/js/jquery.form.js"></script>
        <script type="text/jsx" src="./assets/js/jquery.validate.min.js"></script>
        <script type="text/jsx" src="./assets/js/mail-script.js"></script>
        <script type="text/jsx" src="./assets/js/jquery.ajaxchimp.min.js"></script>

        {/* Jquery Plugins, main Jquery */}
        <script type="text/jsx" src="./assets/js/plugins.js"></script>
        <script type="text/jsx" src="./assets/js/main.js"></script>

        {/* Jquery Mask - Igor Escobar*/}
        <script type="text/jsx" src="./assets/js/jquery.mask.min.js"></script>

        {/* Mascaras para os formularios */}
        <script type="text/jsx" src="./assets/js/mascaras-usuario.js"></script>

        {/* Jquery + AJAX Busca com autocomplete */}
        <script type="text/jsx" src="https://code.jquery.com/jquery-3.6.0.js"></script>
        <script type="text/jsx" src="https://code.jquery.com/ui/1.13.0/jquery-ui.js"></script>
      </Helmet>
  )
}

export default JsImport