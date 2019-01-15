from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/main", methods=["POST"])
def hello():
    first = request.form.getlist("n")
    
    return render_template("main.html", name=first)
