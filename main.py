
from flask import Flask, render_template, request, redirect, session, flash, url_for
app = Flask(__name__)

app.secret_key = 'abobado'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

class usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha
        


jogo1 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo2 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2]

user1 = usuario('Josias', 'Caias', 'esnupi')
user2 = usuario('Gabriela', 'Drudi', 'flor')
user3 = usuario('Gilso', 'Duck', 'charles')

usuarios = {user1.nickname : user1,
           user2.nickname : user2,
           user3.nickname : user3}

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/novo')
def novo():
    if 'Usuario_Logado' not in session or session ['Usuario_Logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/')
def index():
    return render_template('lista.html', jogos = lista, titulo ='Jogos:')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def authenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['Usuario_Logado'] = usuario.nickname
            flash(usuario.nickname + 'logado com sucesso ')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Usuario não logado')
            return redirect(url_for('login'))



@app.route("/logout")
def logout():
    session['Usuario_Logado'] = None
    flash('Logout efetuado')

    return redirect(url_for('index'))

app.run()
