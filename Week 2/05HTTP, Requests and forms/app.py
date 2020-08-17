from flask import request, Flask, render_template 
app = Flask(__name__)  
  
@app.route('/login',methods = ['GET', 'POST'])  
def login():  
   if request.method == 'POST': 
   # i.e. when the user presses the submit button on the website. This checks for any POST requests from the website.
      uname=request.form.get('uname')  
      passwrd=request.form.get('pass') 
      if uname=="Synergy" and passwrd=="Synergy":  
            return f"Welcome {uname}"
   return render_template('index.html') 
   
if __name__ == '__main__':  
   app.run(debug = True) 
