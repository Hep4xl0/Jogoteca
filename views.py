from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from main import app
from models import *
from helpers import recupera_imagem, deleta_arquivo
import time
from view_user import *

@app.route('/criar', methods=['POST',])
def criar():
    form= FormularioJogo(request.form)
    if form.validate_on_submit():
        return redirect(url_for('novo'))
    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data

    jogo = jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo já existente!')
        return redirect(url_for('index'))

    novo_jogo = jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time

    arquivo.save(f'{upload_path}/capa{novo_jogo.id} -- {timestamp}.jpg')

    return redirect(url_for('index'))


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioJogo()
    return render_template('novo.html', titulo='Novo Jogo', form=form)


@app.route('/')
def index():
    lista = jogos.query.order_by(jogos.id)
    return render_template('lista.html', jogos = lista, titulo ='Jogos:')


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar'), id=id))
    jogo = jogos.query.filter_by(id=id).first()
    form = FormularioJogo
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console

    capa_jogo = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Jogo', id=id, capa_jogo=capa_jogo, form=form)

@app.route('/atualizar', methods=['POST',])
def atualizar():
    form = FormularioJogo(request.form)

    if form.validate_on_submit():

        jogo = jogos.query.filter_by(id=request.form['id']).first()
        jogo.nome = form.nome.data
        jogo.categoria = form.nome.data
        jogo.console = form.nome.data

        db.session.add(jogo)
        db.session.commit()

        arquivo = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        deleta_arquivo(jogo.id)
        timestamp = time.time()
        arquivo.save(f'{upload_path}/capa{jogo.id}--{timestamp}.jpg')

    return redirect(url_for('index'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    jogos.query.filter_by(id=id).delete
    db.session.commit()
    flash('Item foi deletado')
    return redirect(url_for('index'))


@app.route('/upload/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)



