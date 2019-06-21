from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    m = []
    o = []
    c = []

    for i in range(100):
        m.append(i)
    for i in range(202):
        o.append(i)
    for i in range(21):
        c.append(i)
    
    random.shuffle(m)
    random.shuffle(o)
    random.shuffle(c)

    return render_template("index.html",m=m,o=o,c=c)


@app.route("/main")
def hello():
    first = request.args.getlist("n")
    
    m = request.args.getlist("m")

    o = request.args.getlist("o")

    c = request.args.getlist("c")
    
    return render_template("main.html", rand=m, rand2=o, rand3=c, name=first)
