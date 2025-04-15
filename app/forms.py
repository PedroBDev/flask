from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField    
from wtforms.validators import DataRequired, Email
from app.models import Contato
from app import db

class ContatoForm(FlaskForm):
      nome = StringField('Nome', validators=[DataRequired()])
      email = StringField('Email', validators=[DataRequired(), Email()])
      assunto = StringField('Assunto', validators=[DataRequired()])
      mensagem = StringField('Mensagem', validators=[DataRequired()])
      btnSubmit= SubmitField('Salvar')

      def save(self):
        contato = Contato(
        nome=self.nome.data, 
        email=self.email.data, 
        assunto=self.assunto.data, 
        mensagem=self.mensagem.data)

        db.session.add(contato)
        db.session.commit()