from app import app
from flask import render_templates

@app.route('/')
def index():
    return render_templates('index.html', name='Keanu')

@app.route('/favorite')
def favorite():
    favorite_artists = [
        ('Avenged Sevenfold')
        ('Slipknot')
        ('Three Days Grace')
        ('Skillet')
        ('Five Finger Death Punch')
    ]
    return render_templates('favorites.html', name='Keanu', artists=favorite_artists)