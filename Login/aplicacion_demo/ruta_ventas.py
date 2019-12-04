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
    tarjetas = Tarjeta.get_all()
    return render_template("venta/crear.html",
                           tarjetas=tarjetas,
                           titulo='Crear nueva')

@app.route("/venta/crear", methods=["POST"])
def vent_agregar():
    if request.method == 'POST':
        monto = request.form.get('monto')
        tarjetas = request.form.getlist('tarjetas')
    if monto and int(monto) > 0 :
        vent = Venta(monto=monto)
        db.session.add(vent)
        db.session.commit()
        for tarjeta_id in tarjetas:
            tarjeta = Tarjeta.find_by_id(tarjeta_id)
            tarjeta.ventas2.append(vent)
            tarjeta.update()
    else:
        return render_template('/venta/error.html')
    return redirect(url_for('venta'))

@app.route('/venta/delete')
def vent_delete():
    venta_id = int(request.args['id'])
    venta = Venta.find_by_id(venta_id)
    db.session.delete(venta)
    db.session.commit()
    return redirect('/venta')

@app.route('/venta/update', methods=['GET', 'POST'])
def vent_update():
    venta_id = int(request.args['id'])
    venta = Venta.find_by_id(venta_id)
    if request.method == 'POST':
        venta.monto = request.form.get('monto')
        db.session.commit()
        return redirect('/venta')
    else:
        return render_template('/venta/update.html', venta=venta)

