import flask
from flask import Flask # importing the Flask module  

app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return f'Hello {name}!'

if __name__ == '__main__':
   app.run(debug = True)
