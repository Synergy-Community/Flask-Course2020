from flask import Flask, Response

app = Flask(__name__)

@app.route('/home/<name>')
def index(name):
    print(name)
    return 'This is your name :{}'.format(name)

@app.route('/about', methods = ['GET','POST'])
def about():
    return Response('<h1>this is about page</h1><p>hii</p>')

@app.route('/age/<int:age>')  
def home(age):  
    return "Age = {}".format(age);  

if __name__=='__main__':
    app.run(debug=True)