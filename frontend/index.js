import React from 'react'
import { AppContainer } from 'react-hot-loader'
import { render } from 'react-dom'

import App from './src/App'
import './src/styles/app.scss'

render(
  <AppContainer>
    <App />
  </AppContainer>,
  document.getElementById('app')
)

if (module.hot) {
  module.hot.accept()
}
