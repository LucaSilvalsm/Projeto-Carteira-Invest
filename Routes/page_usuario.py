from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user,logout_user
from Controller.UsuarioController import UsuarioController
from Model.Usuario import Usuario
from Model import db

user_bp = Blueprint('user_bp', __name__)

@user_bp.before_app_request
def init_usuario_controller():
    global usuarioController
    usuarioController = UsuarioController()

@user_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        senha = request.form['senha']
        cpf = request.form['cpf']
        confirmsenha = request.form['confirmsenha']

        # Verifica se o email já está cadastrado
        if usuarioController.buscar_por_email(email):
            flash('Este email já está sendo utilizado.', 'error')
            return redirect(url_for('page_bp.cadastro'))
        
        # Verifica se o CPF já está cadastrado
        if usuarioController.buscar_por_cpf(cpf):
            flash('Este CPF já está sendo utilizado.', 'error')
            return redirect(url_for('page_bp.cadastro'))

        # Verifica se as senhas coincidem
        if senha != confirmsenha:
            flash('As senhas não coincidem.', 'error')
            return redirect(url_for('page_bp.cadastro'))

        usuario = Usuario(nome, sobrenome, email, senha, cpf)
        usuarioController.incluir(usuario)

        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('page_bp.login'))

    return render_template('login.html')

@user_bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    # Verificar se o email e senha estão presentes
    if email and senha:
        # Buscar o usuário pelo email
        usuario = usuarioController.buscar_por_email(email)

        # Verificar se o usuário existe e a senha está correta
        if usuario and usuario.verificar_senha(senha):
            # Autenticar o usuário usando Flask-Login
            login_user(usuario)

            # Redirecionar para a página teste.html
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('page_bp.painel'))

        # Se o email ou senha estiverem incorretos
        flash('Credenciais inválidas. Verifique seu email e senha.', 'error')

    else:
        flash('Por favor, forneça seu email e senha.', 'error')

    return redirect(url_for('page_bp.login')) 
@user_bp.route('/logout')
def logout():
    # Utiliza o método do Flask-Login para deslogar o usuário
    logout_user()

    # Flash message opcional para informar o usuário que ele foi deslogado com sucesso
    flash('Você foi deslogado com sucesso.', 'success')

    # Redireciona para a página de login, ou para onde desejar após o logout
    return redirect(url_for('page_bp.index'))
    