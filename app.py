from flask import Flask, request, render_template, redirect

app = Flask(__name__)

REGISTRANTS = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods = ["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    REGISTRANTS[name] = sport
    return redirect("./registrants")

@app.route("./registrants")
def registrants():
    return render_template("registrants.html")