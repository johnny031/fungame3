from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    ran = []
    ran2 = []
    ran3 = []

    for i in range(100):
        ran.append(i)
    for i in range(202):
        ran2.append(i)
    for i in range(21):
        ran3.append(i)
    
    random.shuffle(ran)
    random.shuffle(ran2)
    random.shuffle(ran3)

    return render_template("index.html",ran=ran,ran2=ran2,ran3=ran3)


@app.route("/main")
def hello():
    first = request.args.getlist("n")
    
    ran = request.args.getlist("ran")
    rand = ran[0:len(first)*4]

    ran2 = request.args.getlist("ran2")
    rand2 = ran2[0:len(first)*4]

    ran3 = request.args.getlist("ran3")
    rand3 = ran3[0:6]
    
    return render_template("main.html", rand=rand, rand2=rand2, rand3=rand3, name=first)
