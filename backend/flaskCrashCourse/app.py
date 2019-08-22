from flask import Flask, escape, request
import json 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

# Making another route
@app.route('/marvel')
def iron_man():
    return 'And I, am Iron Man'

# Getting parameters from the url and processing it
# Returns a name
@app.route('/<username>')
def profile(username):
    return username

# @app.route('/type/<int:checkType>')
# def check_type(checkType):
#     return type(checkType)

# Adding two numbers together
@app.route('/type/<int:var_a>/<int:var_b>')
def add_two(var_a, var_b):
    return str(var_a + var_b)

# Post request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #json.loads(param) turns json string into a dictionary
        data = json.loads(request.data)
        # Return the messages as a string
        return str( data['message'] + data['message2'] )
    else:
        return 'World'

if __name__ == '__main__':
    app.run(debug=True)

# Install pip globally