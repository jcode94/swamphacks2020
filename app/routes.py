from flask import render_template
from flask import redirect
from flask import url_for
from app import app
from app.forms import LoginForm


@app.route("/")
def index():
    return render_template("Reggie.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return         
    return render_template("login.html", form=form)
