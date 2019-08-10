from flask import render_template
from app import app

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