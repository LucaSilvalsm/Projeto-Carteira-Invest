# Controller/page_controller.py
from flask import Blueprint, render_template, redirect, url_for, session,request
from Model.Usuario import Usuario
from Model.Ativos import Ativos
from Model.config import DATABASE
from sqlalchemy.orm import sessionmaker
from flask_login import current_user,login_required
from sqlalchemy import create_engine
from Controller.AtivosController import AtivosController
import locale





page_bp = Blueprint('page_bp', __name__)
DB_URL = f"postgresql://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

@page_bp.route('/')
def index():
   
    return render_template("index.html")

@page_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@page_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template("cadastro.html")

@login_required
@page_bp.route('/painel')

def painel():
    ativosController = AtivosController()
    usuario_id = current_user.id

    # Calcula o valor atualizado dos investimentos sem alterar o banco
    valor_atualizado = ativosController.valor_investido_atualizado(usuario_id)
    
    # Calcula o valor total investido originalmente
    valor_total_investido = ativosController.valor_total_investido(usuario_id)
    
    # Calcula os dividendos recebidos
    dividendo_recebidos = ativosController.soma_dividendos_recebidos(usuario_id)
    
    # Calcula a rentabilidade (valor atualizado - valor total investido)
    rentabilidade = (valor_atualizado - valor_total_investido) + dividendo_recebidos 

    return render_template("./painel/painel.html", 
                           valor_total_investido=f"R$ {valor_total_investido:,.2f}",
                           dividendo_recebidos=f"R$ {dividendo_recebidos:,.2f}",
                           valor_atualizado=f"R$ {valor_atualizado:,.2f}",
                           rentabilidade=f"R$ {rentabilidade:,.2f}")

@page_bp.route('/ativos')
def ativos():
    print("Acessando a página de ativos.html")
    return render_template("./painel/ativos.html")