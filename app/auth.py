from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Usuario
from . import Session

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        with Session() as session:
            user = session.query(Usuario).filter_by(username=username).first()

        if user and user.password == password:  # En producción, usá hash seguro, no texto plano
            login_user(user)
            flash('Login exitoso')
            return redirect(url_for('routes.index'))
        else:
            flash('Usuario o contraseña incorrectos')

    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada')
    return redirect(url_for('auth.login'))
