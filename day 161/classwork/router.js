import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Auth from './components/Auth';
import Dashboard from './components/Dashboard';
import TaskStats from './components/TaskStats';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" component={Auth} />
        {<Route path="/dashboard" component={Dashboard} />
        <Route path="/taskstats" component={TaskStats} />}
      </Switch>
    </Router>
  );
};

export default App;
