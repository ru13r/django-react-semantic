import React from 'react';
import ReactDOM from 'react-dom'
import {AppContainer} from 'react-hot-loader'

import App from './semantic-react-sample'

ReactDOM.render(
    <AppContainer>
        <App/>
    </AppContainer>,
    document.getElementById('react-test'),
);

if (module.hot) {
    module.hot.accept('./semantic-react-sample', () => {
        const NextApp = require('./semantic-react-sample').default;
        ReactDOM.render(
            <AppContainer>
                <NextApp/>
            </AppContainer>,
            document.getElementById('react-test'),
        );
    });
}
