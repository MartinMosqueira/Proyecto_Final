from flask import request, render_template, redirect, url_for, make_response
from datetime import datetime as dt
from flask import current_app as app
from .modelos import db, Credit

@app.route('/tarjetas/')
def tarjetas():
    tarjetas = Credit.get_all()
    return render_template("personas/tarjetas.html",
                           tarjetas=tarjetas,
                           titulo='tarjetas')

@app.route("/personas/tarjetas", methods=["GET"])
def tarjeta_crear():
    tarjetas = Credit.get_all()
    return render_template("personas/tarjetas.html",
                           tarjetas=tarjetas,
                           titulo='Crear nuevo')

