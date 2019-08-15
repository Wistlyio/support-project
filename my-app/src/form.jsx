import React, { Component } from "react";
import "./form.css";

class Form extends Component {
    state = {
        counter: 1
    };

  render() {
    return <div>
        <h1>
            {this.state.counter}
        </h1>
        </div>
  }
}

export default Form;
