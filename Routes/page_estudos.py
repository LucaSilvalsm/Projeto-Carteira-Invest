from flask import Blueprint, request, flash, redirect, url_for
from flask_login import current_user
from sqlalchemy.orm import sessionmaker
from Model import db
from Controller.EstudosController import EstudosController
from Model.Usuario import Usuario
from Model.Estudos import Estudos
from sqlalchemy.orm import Session


estudos_bp = Blueprint('estudos_bp', __name__)
session = Session()


def carregar_usuario(user_id):
    with Session() as session:
        return session.get(Usuario, user_id)

@estudos_bp.route("/carteira_estudo", methods=["POST"])
def carteira_estudo():
    if request.method == "POST":
        ticket_escolhido = request.form["ticket_escolhido"]
        media_rendimentos = request.form["media_rendimentos"]
        media_recebido = request.form["media_recebido"]
        preco_pessoal = request.form["preco_pessoal"]
        
        # Verificar se os valores são válidos
        if not ticket_escolhido:
            flash("O ticket não pode ser vazio", "error")
            return redirect(url_for('page_bp.carteira_estudos'))

        try:
            media_rendimentos = float(media_rendimentos)
            media_recebido = float(media_recebido)
            preco_pessoal = float(preco_pessoal)
        except ValueError:
            flash("Os valores fornecidos devem ser numéricos", "error")
            return redirect(url_for('page_bp.carteira_estudos'))

        usuario_id = current_user.id
        
        estudos = Estudos(
            ticket_escolhido=ticket_escolhido,
            usuario_id=usuario_id,
            media_rendimentos=media_rendimentos,
            media_recebido=media_recebido,
            preco_pessoal=preco_pessoal
        )
        
        estudosController = EstudosController()
        estudosController.incluir(estudos)
        
        print(estudos)
        flash("Ativo adicionado à carteira de estudo com sucesso", "success")
        return redirect(url_for('page_bp.carteira_estudos'))

@estudos_bp.route("/deletar_estudo", methods=["POST", "GET"])
def deletar_estudo():
    if request.method == "POST":
        ticket_escolhido = request.form['ticket_escolhido']
        print(f"Ticket Escolhido (Formulário): {ticket_escolhido}")  # Depuração
        
        if not ticket_escolhido:
            flash("O ticket não pode ser vazio", "error")
            return redirect(url_for('page_bp.carteira_estudos'))
        
        estudosController = EstudosController()
        usuario_id = current_user.id
        estudo_id = estudosController.buscar_id_ativo_por_ticket(ticket_escolhido, usuario_id)
        
        if estudo_id:
            estudosController.excluir(estudo_id)
            flash("Ativo deletado da carteira de estudo com sucesso", "success")
        else:
            flash("Ativo não encontrado", "error")
        
        return redirect(url_for('page_bp.carteira_estudos'))
