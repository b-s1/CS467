from flask import Flask
app = Flask(__name__)

HOST = '0.0.0.0'
PORT = 5454

# route to index
@app.route('/')
def index():
   return 'Index Page'

# here is an example of basic routing without a page template
@app.route('/hello')
def hello_world():
   return 'Hello, World!'

# this route demonstrates the use of a variable retrieved from the site path
# the variable name is surrounded by angle brackets and then passed into the 
# routing function as a parameter
@app.route('/<routing>')
def variable_routing(routing):
   return 'This is the {} page'.format(routing)

if __name__ == '__main__':
   app.run(host=HOST, port=PORT)
