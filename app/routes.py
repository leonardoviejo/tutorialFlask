from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')

@app.route('/index')
def index():
    user = {'username': 'Leonardo'}
    posts = [
        {
            'author': {'username': 'Claudia'},
            'body': 'Hermoso día en La Plata'
        },
        {
            'author': {'username': 'Susana'},
            'body': 'Hoy juega Argentina'
        }
    ]
    return render_template('index.html', title='Inicio', user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Inicio de sesion requerido para el usuario {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect (url_for('index'))
    return render_template('login.html', title='Iniciar sesión', form=form)