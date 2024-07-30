from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from main import app
from models import *
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash



@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
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