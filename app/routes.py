from app import app
from flask import render_template #renderiza arquivos html

@app.route('/')
def homepage():
    return render_template('index.html')
