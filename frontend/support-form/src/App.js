import React, { Component } from "react";
import { Form, Input, Button } from "antd";

import "antd/dist/antd.css";
import "./App.css";

const axios = require("axios");

class SupportForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
      issue: "",
      email: "",
      info: ""
    };
  }
  //IMPLEMENT AXIOS HERE
  handleSubmit = e => {
    console.log(this.state)
    axios.get('https://cat.requestcatcher.com', this.state
    )
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
    alert(
      `${this.state.name} ${this.state.issue} ${this.state.email} ${this.state.info}`
    );
    e.preventDefault();
  };

  handleNamechange = event => {
    this.setState({ name: event.target.value });
  };
  handleIssuechange = event => {
    this.setState({ issue: event.target.value });
  };
  handleEmailchange = event => {
    this.setState({ email: event.target.value });
  };
  handleInfochange = event => {
    this.setState({ info: event.target.value });
  };

  render() {
    return (
      <Form className="App" onSubmit={this.handleSubmit}>
        <Form.Item label="First and last name" className="inputbox">
          <Input 
          onChange={this.handleNamechange}
          value={this.state.name} 
          size="large" 
          placeholder="Name (ex. John Smith)" 
          />
        </Form.Item>
        <Form.Item label="Summary of issue" className="inputbox">
          <Input
          onChange={this.handleIssuechange}          
          value={this.state.issue}  
          size="large" 
          placeholder="What do you need help with?" 
          />
        </Form.Item>
        <Form.Item label="Email address used" className="inputbox">
          <Input
          onChange={this.handleEmailchange}                  
          value={this.state.email}   
          size="large" 
          placeholder="Email address" 
          type="email" 
          />
        </Form.Item>
        <Form.Item label="Additional info/details" className="textbox">
          <Input.TextArea
          onChange={this.handleInfochange}                  
          value={this.state.info}    
          />
        </Form.Item>
        <Button type="primary" htmlType="submit" className="login-form-button">
          Submit
        </Button>
      </Form>
    );
  }
}

export default SupportForm;
