from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato
from models.avaliacao import Avaliacao
from functools import wraps
 
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
 
from models.usuario import Usuario
from repositories import avaliacao_repo
from repositories import cardapio_repo
from repositories import restaurante_repo
from repositories import usuario_repo

app = Flask(__name__)
app.secret_key = 'uiuiuichavedificildelembr@r'

def login_required(funcao):
    @wraps(funcao)
    def verificar(*args, **kwargs):
        if 'id_usuario' not in session:
            return redirect(url_for('login'))
        return funcao(*args, **kwargs)
    return verificar

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha_hash = generate_password_hash(request.form['senha'])
        if usuario_repo.buscar_email(email) is not None:
            return render_template('cadastro.html', erro="Este e-mail já esta cadastrado.")
        usuario = Usuario(nome, email, senha_hash)
        usuario_repo.criar_usuario(usuario)
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = usuario_repo.buscar_email(email)
        if usuario and check_password_hash(usuario._senha_hash, senha):
            session['id_usuario'] = usuario.id
            return redirect(url_for('painel'))
        return render_template('login.html', erro='Email ou senha inválido.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('id_usuario', None)
    return redirect(url_for('login'))

@app.route('/painel')
@login_required
def painel():
    usuario = usuario_repo.buscar_id(session['id_usuario'])
    return render_template('painel.html', usuario=usuario)

@app.route('/restaurantes')
@login_required
def restaurantes():
    lista_restaurantes = restaurante_repo.listar_restaurantes()
    return render_template('restaurantes.html', restaurantes=lista_restaurantes)

@app.route('/restaurante/<int:id_restaurante>/avaliar', methods=['GET', 'POST'])
@login_required
def avaliar_restaurante(id_restaurante):
    restaurante = restaurante_repo.listar_id_restaurante(id_restaurante)
    if restaurante is None:
        return redirect(url_for('restaurantes'))

    if request.method == 'POST':
        cliente = request.form['cliente']
        nota = float(request.form['nota'])
 
        avaliacao = Avaliacao(cliente, nota)
        avaliacao_repo.criar_avaliacao(id_restaurante, avaliacao)
        return redirect(url_for('listar_avaliacoes', id_restaurante=id_restaurante))

    return render_template('avaliar.html', restaurante=restaurante)

@app.route('/restaurante/<int:id_restaurante>/avaliacoes')
@login_required
def listar_avaliacoes(id_restaurante):
    restaurante = restaurante_repo.listar_informacoes(id_restaurante)
    if restaurante is None:
        return redirect(url_for('restaurantes'))
    return render_template('avaliacoes.html', restaurante=restaurante)

@app.route('/restaurante/<int:id_restaurante>/cardapio')
@login_required
def listar_cardapio(id_restaurante):
    restaurante = restaurante_repo.listar_id_restaurante(id_restaurante)
    if restaurante is None:
        return redirect(url_for('restaurantes'))
    cardapio = cardapio_repo.listar_por_restaurante(id_restaurante)

    pratos = [item for item in cardapio if isinstance(item, Prato)]
    bebidas = [item for item in cardapio if isinstance(item, Bebida)]

    return render_template('cardapio.html', restaurante=restaurante, pratos=pratos, bebidas=bebidas)

if __name__ == '__main__':
    restaurante_repo.tabela_restaurante()
    avaliacao_repo.tabela_avaliacao()
    cardapio_repo.tabela_cardapio()
    usuario_repo.tabela_usuario()
 
    app.run(debug=True)
