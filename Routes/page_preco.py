from flask import Blueprint, render_template, request, flash, redirect, url_for

from flask_login import  current_user
from Model.Usuario import Usuario
from sqlalchemy.orm import Session
from Controller.PrecoController import PrecoController
from Controller.AtivosController import AtivosController
from Model.Preco_teto import Preco_teto



session = Session()
preco_bp = Blueprint('preco_bp', __name__)

@preco_bp.before_app_request
def init_usuario_controller():
    global precoController
    precoController = PrecoController()


def carregar_usuario(user_id):
    return session.get(Usuario, user_id)


@preco_bp.route("/preco_teto", methods=["POST"])
def preco():
    if request.method == "POST":
        ticket = request.form['ticket_ativo']
        media_dividendos = float(request.form['media_dividendos'])
        media_recebido = float(request.form['media_recebido'])
        preco_pessoal = float(request.form['preco_pessoal'])
        
        ativos_controller = AtivosController()
        usuario_id = current_user.id
        
        ativo_id = ativos_controller.buscar_id_ativo_por_ticket(ticket, usuario_id)
        print(ativo_id)
        
        
        preco_teto = Preco_teto(
            ticket = ticket,
            media_dividendos = media_dividendos,
            media_recebido = media_recebido,
            preco_pessoal = preco_pessoal,
            ativo_id = ativo_id,
            usuario_id = usuario_id
            
        )
        
        precoController.incluir(preco_teto)
        flash('Preco teto cadastrado com sucesso!', 'success')
        return redirect(url_for('page_bp.calcular_preco'))

        







