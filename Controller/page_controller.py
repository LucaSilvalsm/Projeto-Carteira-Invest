# Controller/page_controller.py
from flask import Blueprint, render_template, redirect, url_for, session,request
from Model.Usuario import Usuario
from Model.Ativos import Ativos
from Model.config import DATABASE
from sqlalchemy.orm import sessionmaker
from flask_login import current_user,login_required
from sqlalchemy import create_engine
from Controller.AtivosController import AtivosController





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
    
    valor_total_investido = ativosController.valor_total_investido(usuario_id)
    dividendo_recebidos = ativosController.soma_dividendos_recebidos(usuario_id)
    return render_template("./painel/painel.html", valor_total_investido=valor_total_investido, dividendo_recebidos=dividendo_recebidos)

@page_bp.route('/ativos')
def ativos():
    print("Acessando a página de ativos.html")
    return render_template("./painel/ativos.html")