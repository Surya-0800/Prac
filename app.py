from flask import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tODO.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default= datetime.utcnow)

    def __repr__(self):
        return f"{self.sno}-{self.title}"


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    todo = Todo(title = "First Todo",desc="Start Investing")
    db.session.add(todo)
    db.session.commit()
    return "This is Products Page"



if __name__ ==  "__main__":
    app.run(debug=True,port=8000)
