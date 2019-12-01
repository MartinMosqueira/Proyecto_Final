from flask import request, render_template, redirect, url_for, make_response
from flask import current_app as app
from .modelos import db, Persona, Tarjeta, Venta

@app.route('/venta/')
def venta():
    ventas = Venta.get_all()
    return render_template("venta/index.html",
                           ventas=ventas,
                           titulo='Ventas')


@app.route("/venta/crear", methods=["GET"])
def vent_crear():
    ventas = Venta.get_all()
    return render_template("venta/crear.html",
                           ventas=ventas,
                           titulo='Crear nueva')

