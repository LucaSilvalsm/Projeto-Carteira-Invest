from flask import Blueprint, request, flash, redirect, url_for
from flask_login import  current_user
from Controller.AtivosController import AtivosController
from sqlalchemy.orm import Session
from Model.Ativos import Ativos
from Model.Usuario import Usuario


ativos_bp = Blueprint('ativos_bp', __name__)
session = Session()
@ativos_bp.before_app_request
def init_usuario_controller():
    global ativosController
    ativosController = AtivosController()

@ativos_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    if request.method == 'POST':
        nome_ativo = request.form['nome_ativo']
        ticket_ativo = request.form['ticket_ativo']
        categoria = request.form['categoria']
        setor = request.form.getlist('setor[]')  # Obtém a lista de setores selecionados
        
        

        # Verificação de depuração para ver os setores selecionados
        

        # Verificar se o usuário selecionou pelo menos um setor
        if not setor:
            flash('Por favor, selecione pelo menos um setor.', 'error')
            return redirect(url_for('page_bp.painel/adicionar_ativos'))

        quantidade = int(request.form['quantidade'])
        preco_medio = float(request.form['preco'])  # Corrigido para 'preco'       
        

        # Criando o objeto Ativos
        
        ativo = Ativos(
            nome_ativo=nome_ativo,
            ticket_ativo=ticket_ativo,
            categoria=categoria,
            setor=setor[0],
            usuario_id=current_user.id,
            quantidade=quantidade,
            preco_medio=preco_medio,  # deve ser float           
            
        )


        # Incluindo o ativo no banco de dados
        ativosController.incluir(ativo)

        flash('Ativo cadastrado com sucesso!', 'success')
        return redirect(url_for('page_bp.ativos'))
def carregar_usuario(user_id):
    return session.get(Usuario, user_id)
