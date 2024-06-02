import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Projects from './components/Projects';

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/projects" component={Projects} />
                    <Route path="/" exact component={Projects} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;

