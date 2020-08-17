from flask import *
app = Flask(__name__)  
@app.route('/admin')  
def admin():  
    return 'admin'  
  
@app.route('/user')  
def user():  
    return 'user'  
  
@app.route('/student')  
def student():  
    return 'student'  
  
@app.route('/work/<name>')  
def work(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'user':  
        return redirect(url_for('user'))  
    if name == 'student':  
        return redirect(url_for('student')) 
 
if __name__ == '__main__':  
    app.run(debug = True)   
