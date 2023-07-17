from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'

# import statements, maybe some other routes

@app.route('/success')
def success():
    return 'success'

#@app.route('/hello/<name>')
#def hello(name):
#   print(name)
#    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + " id: " + id

# Type Converters 
# Another feature of variable rules is the ability to designate an expected type for a route variable. For this you can use what Flask calls 'converters.' By default a route variable is passed as a string, even if the character(s) are numbers. In the example below we designate int as the converter, which indicates that we are expecting an integer to be passed through in that part of the route string. Flask will then cast the argument into the type specified, converting for example, the string '8' into the integer 8.
@app.route('/hello/<name>/<int:num>')
def hello(name,num):
    return f"Hello, {name * num}"


if __name__ =='__main__':
    app.run(debug=True)
# This needs to be the last statement