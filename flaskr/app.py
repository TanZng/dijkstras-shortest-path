from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import services.make_plot
import os

UPLOAD_FOLDER = os.path.abspath("./uploads/")
ALLOWED_EXTENSIONS = set(["txt"])

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

'''
# Base de datos
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app.config['SQLALCHEMY_DATABASE_URI'] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
'''


@app.route('/', methods=["GET", "POST"])
def index():
    name_file = "default.txt"
    titulo = "Grafos!"
    
    if request.method == "POST":

        if not "file" in request.files:
            error = "No file part in the form."

        f = request.files["file"]
        if f.filename == '':
            error = "No file selected. Please select a .txt"
            
        elif f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            name_file = f.filename
            error = "Successful uploaded."

        else:
            error = "File not allowed."
        
    else:
        error= "Seleccione un archivo .txt"
        
    services.make_plot.run("uploads/"+ name_file)
    return render_template("index.html", titulo = titulo, error = error, name_file = name_file)


if __name__ == "__main__":
    #db.create_all()
    app.run(debug=True)