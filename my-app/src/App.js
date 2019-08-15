import React from "react";
import "./App.css";
import { Button, Icon } from "antd";

const picture = "https://i.redd.it/eexdukzbxkg31.jpg";

function App() {
  return (
    <div className="App">
      <img className="doggo" src={picture} height="175" width="175" />
      <a href={picture}>
        <Button className="cat" type="primary">
          {" "}
          cat{" "}
        </Button>
      </a>
    </div>
  );
}

export default App;
