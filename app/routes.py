from flask import render_template
from flask import request
from app import app

@app.route('/', defaults={"nome":"usuário"})
@app.route('/index', defaults={"nome":"usuário"})
@app.route('/index/<nome>')
def index(nome):
  dados = {"profissao": "Desenvolvedor", "canal": "Renan Cruz"}
  return render_template('index.html', nome=nome, dados=dados)


@app.route('/contato')
def contato():
  return render_template('contato.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
  #GET
  # usuario = request.args.get('usuario')
  # senha = request.args.get('senha')

  #POST
  usuario = request.form.get('usuario')
  senha = request.form.get('senha')
  return "usuario: {} e senha: {}".format(usuario, senha)
