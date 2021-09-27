from enum import unique
from flask import Flask,render_template,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/afaru/OneDrive/Masaüstü/hatim2/hatimson.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=='POST':
        service1=request.form['service1']
        service=request.form['service']
        service3=request.form['service3']
        service4=request.form['service4']
        new = users(mintika=service1,kurum=service,hatim=service3,adet=service4)
        db.session.add(new)
        db.session.commit()
        
        
        return redirect(url_for("index"))   



class users(db.Model):
    _id= db.Column(db.Integer,primary_key=True)
    mintika = db.Column(db.String(80))
    kurum = db.Column(db.String(120))
    hatim = db.Column(db.String(30))
    adet = db.Column(db.Integer)
def __init__(self, mintika, kurum, hatim,adet):
   self.mintika = mintika
   self.kurum = kurum
   self.hatim = hatim
   self.adet = adet
    



if __name__=="__main__":
    db.create_all()
    app.run(debug=True)  

    
  


  