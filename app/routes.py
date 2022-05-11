from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  nome = "Renan"
  dados = {"profissao": "Desenvolvedor", "canal": "Renan Cruz"}
  return render_template('index.html', nome=nome, dados=dados)


@app.route('/contato')
def contato():
  return render_template('contato.html')