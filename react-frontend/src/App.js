import { Route, Switch } from "react-router";

import "./App.css";
import Header from "./components/header/Header";
import Main from "./components/body/Main";
import Roasts from "./components/body/Roasts";
import Boasts from "./components/body/Boasts";
import HighRank from "./components/body/HighRank";
import Footer from "./components/footer/Footer";
import NewPost from "./components/newpost/NewPost";

function App() {
  return (
    <div className="App">
      <Header />
      <Switch>
        <Route exact path="/">
          <Main />
        </Route>
        <Route exact path="/roasts">
          <Roasts />
        </Route>
        <Route exact path="/boasts">
          <Boasts />
        </Route>
        <Route exact path="/highranked">
          <HighRank />
        </Route>
        <Route exact path="/newpost">
          <NewPost />
        </Route>
      </Switch>

      <Footer />
    </div>
  );
}

export default App;
