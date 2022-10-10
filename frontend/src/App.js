// styles
import './App.css'
import './assets/css/owl.carousel.min.css'
import './assets/css/flaticon.css'
import './assets/css/slicknav.css'
import './assets/css/animate.min.css'
import './assets/css/magnific-popup.css'
import './assets/css/fontawesome-all.min.css'
import './assets/css/themify-icons.css'
import './assets/css/slick.css'
import './assets/css/nice-select.css'
import './assets/css/style.css'

// components
import Core from './pages/core/Core';
import JsImport from './components/utils/JsImport';


function App() {
  return (
    <>
      <Core />

      {/* JS */}
      <JsImport />
    </>
  );
}

export default App;
