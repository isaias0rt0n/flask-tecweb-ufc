from flask import *  

app = Flask(__name__)  

@app.route('/')  
def home_page ():  
  return render_template("home3.html") 
 
@app.route('/login')   
def login_page():  
  return render_template("login3.html");  

@app.route('/validate', methods = ["POST"])  
def validate():
  if request.method == 'POST' and request.form['pass'] == 'Akash':   
    return redirect(url_for("success"))
  else:
    abort(400) 

@app.route('/success')  
def success():  
   return "logged in successfully"  

if __name__ == '__main__':
  app.run(debug = True) 