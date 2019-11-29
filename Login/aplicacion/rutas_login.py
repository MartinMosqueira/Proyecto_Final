from flask import request, render_template, redirect, url_for, make_response
from datetime import datetime as dt
from flask import current_app as app
from .modelos import db, Login

@app.route('/personas/')
def personas():
    personas = Login.get_all()
    return render_template("personas/crear.html",
                           personas=personas,
                           titulo='personas')

app.route("/personas/", methods=["GET"])
def personas_crear():
    print('request.args')
    print(request.args)
    print('request.base_url')
    print(request.base_url)
    print('request.data')
    print(request.data)
    print('request.form')
    print(request.form)
    print('request.get_json()')
    print(request.get_json())
    print('request.get_data()')
    print(request.get_data())
    print('request.full_path')
    print(request.full_path)
    print('request.headers')
    print(request.headers)
    print('request.method')
    print(request.method)
    print('request.query_string')
    print(request.query_string)
    print('request.referrer')
    print(request.referrer)
    print('request.user_agent')
    print(request.user_agent)
    return render_template("personas/crear.html")

@app.route("/personas/", methods=["POST"])
def persona_agregar():
    if request.method == 'POST':
        Nombre = request.form.get('Nombre')
        Apellido = request.form.get('Apellido')
        Documento = request.form.get('Documento')
    if Nombre and Apellido and Documento:
        pers1 = Login(Nombre=Nombre, Apellido=Apellido, Documento=Documento)
        db.session.add(pers1)
        db.session.commit()
    return redirect(url_for('pers'))