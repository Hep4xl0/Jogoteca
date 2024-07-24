from flask import Flask, render_template, request, redirect, session, flash, url_for
from main import app
from models import *

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo já existente!')
        return redirect(url_for('index'))

    novo_jogo = jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/')
def index():
    lista = jogos.query.order_by(jogos.id)
    return render_template('lista.html', jogos = lista, titulo ='Jogos:')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))
    

@app.route("/logout")
def logout():
    session['Usuario_Logado'] = None
    flash('Logout efetuado')

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar'), id=id))
    jogo = jogos.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editando Jogo', jogo=jogo)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    jogo.id = request.form['id']
    jogo = jogos.query.filter_by(id=jogo_id).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    jogos.query.filter_by(id=id).delete
    db.session.commit()
    flash('Item foi deletado')
    return redirect(url_for('index'))
