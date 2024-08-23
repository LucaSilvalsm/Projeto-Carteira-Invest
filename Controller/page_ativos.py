from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from Controller.AtivosController import AtivosController
from sqlalchemy.orm import Session
from Model.Ativos import Ativos
from Model.Usuario import Usuario
from Model import db
import yfinance as yf  # Corrigido o import do yfinance

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
        print("Setores selecionados:", setor)

        # Verificar se o usuário selecionou pelo menos um setor
        if not setor:
            flash('Por favor, selecione pelo menos um setor.', 'error')
            return redirect(url_for('page_bp.painel/adicionar_ativos'))

        quantidade = int(request.form['quantidade'])
        preco_medio = float(request.form['preco'])  # Corrigido para 'preco'
        dividendos = float(request.form['dividendo'])  # Corrigido para 'dividendo'
        preco_pessoal = float(request.form['preco_pessoal'])

        # Criando o objeto Ativos
        
        ativo = Ativos(
            nome_ativo=nome_ativo,
            ticket_ativo=ticket_ativo,
            categoria=categoria,
            setor=setor[0],
            usuario_id=current_user.id,
            quantidade=quantidade,
            preco_medio=preco_medio,  # deve ser float
            dividendos=dividendos,    # deve ser float
            preco_pessoal=preco_pessoal  # deve ser float
        )


        # Incluindo o ativo no banco de dados
        ativosController.incluir(ativo)

        flash('Ativo cadastrado com sucesso!', 'success')
        return redirect(url_for('page_bp.ativos'))
def carregar_usuario(user_id):
    return session.get(Usuario, user_id)
