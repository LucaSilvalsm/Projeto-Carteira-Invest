from flask import Blueprint, request, flash, redirect, url_for
from flask_login import  current_user
from Controller.RendimentosController import RendimentosController
from Controller.AtivosController import AtivosController
from Model.Usuario import Usuario
from Model.Rendimentos import Rendimentos
from sqlalchemy.orm import Session

from Model import db

rendimentos_bp = Blueprint('rendimentos_bp', __name__)
session = Session()
@rendimentos_bp.before_app_request
def init_usuario_controller():
    global rendimentosController
    rendimentosController = RendimentosController()
  
    
@rendimentos_bp.route('/rendimentos/adicionar', methods=['POST'])
def adicionar():
    if request.method == 'POST':
        nome_ativos = request.form['ticket_ativo']
        valor_recebido = float(request.form['dividendo_recebido'])
        data_dividendo =  request.form['data_dividendo']
        usuario_id = current_user.id
        
        
        ativos_controller = AtivosController()
        ativos_id = ativos_controller.buscar_id_ativo_por_ticket(nome_ativos, usuario_id)
        print(ativos_id)
        rendimentos = Rendimentos(
            nome_ativos = nome_ativos,
            valor_recebido = valor_recebido,
            data_dividendo = data_dividendo,
            ativo_id = ativos_id,
            usuario_id = usuario_id
            
        )
        print(rendimentos)
        rendimentosController.incluir(rendimentos)
        flash('Rendimento cadastrado com sucesso!', 'success')
        return redirect(url_for('page_bp.dividendos'))
    


def carregar_usuario(user_id):
    return session.get(Usuario, user_id)