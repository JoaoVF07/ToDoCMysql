from app import app
from flask import render_template, url_for, request, redirect
from app.models import cursor, conexao

@app.route('/')
def homepage():
    return render_template("Inicio.html")

@app.route('/login')
def page_login():
    return render_template("login.html")

@app.route('/login', methods=['POST', 'GET'])
def login():
    senha = request.form['senha']
    email = request.form['email']

    query = f'SELECT * FROM user WHERE email = "{email}" and senha = "{senha}"'
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return redirect('home')
    return redirect(url_for('page_login'))

@app.route('/cadastro', methods=['GET','POST'])
def page_cadastro():
    return render_template("cadastro.html")

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    senha = request.form['senha']
    email = request.form['email']
    confSenha = request.form['confSenha']
    nome = request.form['nome']

    if senha == confSenha:
        print("Chegou")
        comando = f'INSERT INTO user (nome, email, senha) VALUES ("{nome}", {email},"{senha}")'
        cursor.execute(comando)
        conexao.commit() 
        return redirect(url_for('page_login'))
    return redirect(url_for('page_cadastro'))

@app.route('/inicio')
def home():
    return render_template("home.html")