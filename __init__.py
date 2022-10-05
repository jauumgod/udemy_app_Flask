from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite://app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

class User(db,Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(84),nullalble=False, unique=True)
  password = db.Column(db.String(255), nullable=False)

@app.route("/")
def index():
  return render_template("Index.html")
  
  
if __name__ =="__main__":
  app.run(debug=True)
