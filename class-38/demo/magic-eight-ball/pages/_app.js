import 'tailwindcss/tailwind.css'

import Footer from '../components/Footer'

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Component {...pageProps} />
      <Footer />
    </>
  )
}

export default MyApp
