from app import app, db
from flask import render_template, url_for, request, redirect
from app.models import Contato
from app.forms import ContatoForm

@app.route('/')
def homepage():
    usuario='Mobi Brasil'
    return render_template('index.html', usuario=usuario)




@app.route('/Contato', methods=('GET', 'POST'))
def contato():
    form = ContatoForm()
    context={}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))
    
    return render_template('contato.html', context=context, forms=form)


@app.route('/Contato/lista')
def contatoLista():

    dados = Contato.query.all()
    context={'dados': dados}

    return render_template('contato_lista.html', context=context)

#Formulario via html(para fins de estudo), não é recomendado para aplicações ativas na web, pois é menos seguro.
@app.route('/Contato_old', methods=('GET', 'POST'))
def contato_old():
    context={}
    if request.method== 'GET' :
        pesquisa= request.args.get('pesquisa')#recupera o dado passado na pagina
        context.update({'pesquisa' : pesquisa})
    if request.method=='POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        
        #criando contato(objeto) para adicionar ao db
        contato= Contato(nome=nome, email=email, assunto=assunto, mensagem=mensagem)
        
        #adicionando ao db:
        db.session.add(contato)
        db.session.commit()
    
    return render_template('contato_old.html', context=context)