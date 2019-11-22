from flask import request, render_template, redirect, url_for, make_response
from datetime import datetime as dt
from flask import current_app as app
from .modelos import db, Login

@app.route('/personas/')
def personas():
    personas = Login.get_all()
    return render_template("personas/index.html",
                           personas=personas,
                           titulo='personas')

@app.route("/personas/crear", methods=["GET"])
def persona_crear():
    personas = Login.get_all()
    return render_template("personas/crear.html",
                           personas=personas,
                           titulo='Crear nuevo')


