from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length
from main import db

class FormularioJogo(FlaskForm):
    nome = StringField('Nome Jogo', validators=[DataRequired(), Length(min=1, max=50)])
    categoria = StringField('Categoria Jogo', validators=[DataRequired(), Length(min=1, max=40)])
    console = StringField('Console Jogo', validators=[DataRequired(), Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class jogos(db.Model):  # Classes e nomes de tabelas devem estar em PascalCase
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Nome %r>' % self.nome

class Usuarios(db.Model):  # Classes e nomes de tabelas devem estar em PascalCase
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Nome %r>' % self.nome

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=1, max=8)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=1, max=100)])
    login = SubmitField('Login')