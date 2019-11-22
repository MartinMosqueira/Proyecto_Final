from flask import request, render_template, make_response
from flask import current_app as app

@app.route("/", methods=["GET"])
def pagina_principal():
    return render_template("formulario.html", titulo="Formulario")