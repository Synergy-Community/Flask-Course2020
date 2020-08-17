from flask import Flask, render_template 
app = Flask(__name__) 
  
@app.route("/") 
def index(): 
   return render_template("index.html", user="Synergy!", 
                           my_string="Hey there! I like these colours: ", 
                           my_list=['AUSTRALIEN', 'BANAN', 'AMBER', 'DRAKE’S-NECK', 
                                    'DRUNK-TANK PINK', 'FALU', 'FLAME-OF-BURNT-BRANDY',
                                    'GINGERLINE', 'INCARNADINE', 'LABRADOR', 'LUSTY GALLANT', 
                                    'NATTIER', 'PERVENCHE', 'SANG-DE-BOEUF']) 
# user, my_string and my_list are the variables we pass to the template index.html 
if __name__ == '__main__': 
   app.run(debug = True)
