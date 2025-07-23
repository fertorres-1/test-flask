from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Diario
from . import Session
from datetime import datetime

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return redirect(url_for('routes.diarios'))

@routes.route('/diarios')
def diarios():
    with Session() as session:
        data = session.query(Diario).all()
    return render_template('diarios.html', title="Diarios", data=data)

@routes.route('/add_diarios', methods=['GET', 'POST'])
def add_diarios():
    if request.method == 'POST':
        fecha = request.form.get('fecha')
        actividad = request.form.get('actividad')
        cantidad = request.form.get('cantidad')

        try:
            fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
        except Exception:
            flash("Fecha inválida. Use formato YYYY-MM-DD.")
            return redirect(url_for('routes.add_diarios'))

        try:
            cantidad_val = float(cantidad)
        except Exception:
            flash("Cantidad inválida. Debe ser un número.")
            return redirect(url_for('routes.add_diarios'))

        nuevo = Diario(fecha=fecha_dt, actividad=actividad, cantidad=cantidad_val)

        with Session() as session:
            session.add(nuevo)
            session.commit()

        flash("Registro agregado correctamente.")
        return redirect(url_for('routes.diarios'))

    return render_template('add_diarios.html', title="Agregar Diario")
