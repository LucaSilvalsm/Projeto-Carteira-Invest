# Controller/page_controller.py
from flask import Blueprint, render_template
from Model.Usuario import Usuario
from Model.Ativos import Ativos
from Model.config import DATABASE
from sqlalchemy.orm import sessionmaker
from flask_login import current_user,login_required
from sqlalchemy import create_engine
from flask import request,flash

from Controller.AtivosController import AtivosController
from Controller.RendimentosController import RendimentosController
from Controller.PrecoController import PrecoController
from Controller.EstudosController import EstudosController
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


@page_bp.route('/painel')
@login_required

def painel():
    current_route = 'painel'
    ativosController = AtivosController()
    usuario_id = current_user.id
    rendimentoController = RendimentosController()
    # Calcula o valor atualizado dos investimentos sem alterar o banco
    valor_atualizado = ativosController.valor_investido_atualizado(usuario_id)
    
    # Calcula o valor total investido originalmente
    valor_total_investido = ativosController.valor_total_investido(usuario_id)
    
    # Calcula os dividendos recebidos
    dividendo_recebidos = rendimentoController.soma_dividendos_totais(usuario_id)

    
    # Calcula a rentabilidade (valor atualizado - valor total investido)
    rentabilidade = (valor_atualizado - valor_total_investido) + dividendo_recebidos 
    
    ativos_valorizados = ativosController.ativos_valorizados(usuario_id)
    ativos_desvalorizados = ativosController.ativos_desvalorizados(usuario_id)

    return render_template("./painel/painel.html", 
                           current_route=current_route,
                           valor_total_investido=f"R$ {valor_total_investido:,.2f}",
                           dividendo_recebidos=f"R$ {dividendo_recebidos:,.2f}",
                           valor_atualizado=f"R$ {valor_atualizado:,.2f}",
                           rentabilidade=f"R$ {rentabilidade:,.2f}",
                           ativos_valorizados=ativos_valorizados,
                           ativos_desvalorizados=ativos_desvalorizados)
                           

@page_bp.route('/painel/adicionar_ativos')
@login_required
def ativos():
    current_route = 'adicionar_ativos'
    print("Acessando a página de ativos.html")
    return render_template("./painel/ativos.html",current_route=current_route)


@page_bp.route('/painel/mapa_da_carteira')
@login_required
def mapa():
    current_route = 'mapa_ativos'
    ativosController = AtivosController()
    rendimentosController = RendimentosController()
    usuario_id = current_user.id

    # Calcula o valor atualizado dos investimentos sem alterar o banco
    valor_atualizado = ativosController.valor_investido_atualizado(usuario_id)
    
    # Calcula o valor total investido originalmente
    valor_total_investido = ativosController.valor_total_investido(usuario_id)
    
    # Calcula os dividendos recebidos
    dividendo_recebidos = rendimentosController.soma_dividendos_totais(usuario_id)
    
    # Calcula a rentabilidade (valor atualizado - valor total investido)
    rentabilidade = (valor_atualizado - valor_total_investido) + dividendo_recebidos 
    
    ativos_valorizados = ativosController.ativos_valorizados(usuario_id)
    ativos_desvalorizados = ativosController.ativos_desvalorizados(usuario_id)

    return render_template("./painel/mapa_carteira.html", 
                           current_route=current_route,
                           valor_total_investido=f"R$ {valor_total_investido:,.2f}",
                           dividendo_recebidos=f"R$ {dividendo_recebidos:,.2f}",
                           valor_atualizado=f"R$ {valor_atualizado:,.2f}",
                           rentabilidade=f"R$ {rentabilidade:,.2f}",
                           ativos_valorizados=ativos_valorizados,
                           ativos_desvalorizados=ativos_desvalorizados)


@page_bp.route('/painel/consolidado')
@login_required
def consolidado():
    ativosController = AtivosController()
    rendimentosController = RendimentosController()
    usuario_id = current_user.id
    current_route = 'consolidado'
    # Calcula o valor atualizado dos investimentos sem alterar o banco
    valor_atualizado = ativosController.valor_investido_atualizado(usuario_id)
    
    # Calcula o valor total investido originalmente
    valor_total_investido = ativosController.valor_total_investido(usuario_id)
    
    # Calcula os dividendos recebidos
    dividendo_recebidos = rendimentosController.soma_dividendos_totais(usuario_id)

    
    # Calcula a rentabilidade (valor atualizado - valor total investido)
    rentabilidade = valor_atualizado + dividendo_recebidos - valor_total_investido
    
    # Verifica se valor_total_investido é zero para evitar divisão por zero
    if valor_total_investido == 0:
        rentabilidade_real = 0
    else:
        # Calcula a rentabilidade real em porcentagem
        rentabilidade_real = (rentabilidade / valor_total_investido) * 100

    return render_template(
        "./painel/carteiraConsolidada.html", 
        current_route=current_route,
        valor_total_investido=f"R$ {valor_total_investido:,.2f}",
        dividendo_recebidos=f"R$ {dividendo_recebidos:,.2f}",
        valor_atualizado=f"R$ {valor_atualizado:,.2f}",
        rentabilidade_real=f"{rentabilidade_real:.2f}%"
    )


@page_bp.route("/painel/dividendos")
@login_required

def dividendos():
    ativosController = AtivosController()
    current_route = 'carteira dividendos'
    rendimentosController = RendimentosController()
    usuario_id = current_user.id
    dividendo_recebidos = rendimentosController.soma_dividendos_totais(usuario_id)
    # Calcula o valor atualizado dos investimentos sem alterar o banco
    valor_atualizado = ativosController.valor_investido_atualizado(usuario_id)
    
    # Calcula o valor total investido originalmente
    valor_total_investido = ativosController.valor_total_investido(usuario_id)
    
    rentabilidade = (valor_atualizado - valor_total_investido) + dividendo_recebidos 

    ativos = ativosController.buscar_ativos_por_usuario(usuario_id)
    return render_template("./painel/dividendos.html",ativos=ativos,
                            dividendo_recebidos=f"R$ {dividendo_recebidos:,.2f}",
                            rentabilidade=f"R$ {rentabilidade:,.2f}",
                            valor_atualizado=f"R$ {valor_atualizado:,.2f}",
                            valor_total_investido=f"R$ {valor_total_investido:,.2f}",
                            current_route=current_route)
    
    
@page_bp.route("/painel/preco_teto")
@login_required
def preco_teto():
    ativosController = AtivosController()
    current_route = 'preco_teto'
    rendimentosController = RendimentosController()
    usuario_id = current_user.id
    dividendo_recebidos = rendimentosController.soma_dividendos_totais(usuario_id)
    # Calcula o valor atualizado dos investimentos sem alterar o banco
    valor_atualizado = ativosController.valor_investido_atualizado(usuario_id)
    
    # Calcula o valor total investido originalmente
    valor_total_investido = ativosController.valor_total_investido(usuario_id)
    
    rentabilidade = (valor_atualizado - valor_total_investido) + dividendo_recebidos 

    ativos = ativosController.buscar_ativos_por_usuario(usuario_id)
    return render_template("./painel/preco_teto.html",ativos=ativos,
                            dividendo_recebidos=f"R$ {dividendo_recebidos:,.2f}",
                            rentabilidade=f"R$ {rentabilidade:,.2f}",
                            valor_atualizado=f"R$ {valor_atualizado:,.2f}",
                            valor_total_investido=f"R$ {valor_total_investido:,.2f}",
                            current_route=current_route)
    

@page_bp.route("/painel/calcular_preco")
@login_required
def calcular_preco():
    current_route = 'calcular_preco'
    ativosController = AtivosController()
    rendimentosController = RendimentosController()
    usuario_id = current_user.id
    
    dividendo_recebidos = rendimentosController.soma_dividendos_totais(usuario_id)
    valor_atualizado = ativosController.valor_investido_atualizado(usuario_id)
    valor_total_investido = ativosController.valor_total_investido(usuario_id)
    rentabilidade = (valor_atualizado - valor_total_investido) + dividendo_recebidos

    ativos = ativosController.buscar_ativos_por_usuario(usuario_id)
    
    precoController = PrecoController()
    preco_teto_dados = precoController.calcular_preco_teto_por_usuario(usuario_id)
    preco_positivo = precoController.calcular_preco_teto_positiva(usuario_id)
    preco_negativo = precoController.calcular_preco_teto_negativo(usuario_id)
    
    try:
        preco_teto_dados = precoController.calcular_preco_teto_por_usuario(usuario_id)
    except Exception as e:
        print(f"Erro ao calcular preço teto: {e}")
        preco_teto_dados = {}
        preco_positivo = {}
        preco_negativo = {}
   
   
    def formatar_dados(dados):
        for ticket, info in dados.items():
            info['cotacao_atual'] = f"R$ {info['cotacao_atual']:.2f}" if info['cotacao_atual'] is not None else 'N/A'
            info['media_dividendos'] = f"{info['media_dividendos']:.1f}%"
            info['media_recebido'] = f"R$ {info['media_recebido']:.2f}"
            info['preco_pessoal'] = f"R$ {info['preco_pessoal']:.2f}"
            info['margem_pessoal'] = f"{info['margem_pessoal']:.2f}%"
            info['preco_teto_calculado'] = f"R$ {info['preco_teto_calculado']:.2f}"
            
            # Converter margem_de_seguranca para float e formatar como porcentagem
            try:
                margem = float(info['margem_de_seguranca'])
                info['margem_de_seguranca'] = f"{margem:.2f}%"
            except ValueError:
                info['margem_de_seguranca'] = 'N/A'

    # Formatar os dados para o HTML
    formatar_dados(preco_teto_dados)
    formatar_dados(preco_positivo)
    formatar_dados(preco_negativo)

    return render_template("./painel/calcular_preco.html",
                           ativos=ativos,
                           dividendo_recebidos=f"R$ {dividendo_recebidos:,.2f}",
                           rentabilidade=f"R$ {rentabilidade:,.2f}",
                           valor_atualizado=f"R$ {valor_atualizado:,.2f}",
                           valor_total_investido=f"R$ {valor_total_investido:,.2f}",
                           current_route=current_route,
                           preco_teto=preco_teto_dados,
                           preco_positivo=preco_positivo,
                           preco_negativo=preco_negativo)


@page_bp.route("/painel/carteira_estudos")
@login_required
def carteira_estudos():
    current_route = 'carteira_estudos'
    ativosController = AtivosController()
    rendimentosController = RendimentosController()
    estudosController = EstudosController()
    usuario_id = current_user.id
    
    dividendo_recebidos = rendimentosController.soma_dividendos_totais(usuario_id)
    valor_atualizado = ativosController.valor_investido_atualizado(usuario_id)
    valor_total_investido = ativosController.valor_total_investido(usuario_id)
    rentabilidade = (valor_atualizado - valor_total_investido) + dividendo_recebidos
    preco_teto_positiva = estudosController.calcular_preco_teto_positiva_por_usuario(usuario_id)
    preco_teto_negativa = estudosController.calcular_preco_teto_negativa_por_usuario(usuario_id)

    try:
        acoes = estudosController.buscar_ativos_por_usuario(usuario_id)
    except Exception as e:
        print(f"Erro ao buscar ativos: {e}")
        acoes = []  # Ou outro valor padrão

    try:
        preco_teto_dados = estudosController.calcular_preco_teto_por_usuario(usuario_id)
    except Exception as e:
        print(f"Erro ao calcular preço teto: {e}")
        preco_teto_dados = {}
        preco_teto_positiva = {}
        preco_teto_negativa = {}
    
    # Formatar os dados para o HTML
    
    def formatar_dados(dados):
        for ticket, info in dados.items():
            info['cotacao_atual'] = f"R$ {info['cotacao_atual']:.2f}" if info['cotacao_atual'] is not None else 'N/A'
            info['media_dividendos'] = f"{info['media_dividendos']:.1f}%"
            info['media_recebido'] = f"R$ {info['media_recebido']:.2f}"
            info['preco_pessoal'] = f"R$ {info['preco_pessoal']:.2f}"
            info['margem_pessoal'] = f"{info['margem_pessoal']:.2f}%"
            info['preco_teto_calculado'] = f"R$ {info['preco_teto_calculado']:.2f}"
            
            # Converter margem_de_seguranca para float e formatar como porcentagem
            try:
                margem = float(info['margem_de_seguranca'])
                info['margem_de_seguranca'] = f"{margem:.2f}%"
            except ValueError:
                info['margem_de_seguranca'] = 'N/A'
    # Formatar os dados para o HTML
    formatar_dados(preco_teto_dados)
    formatar_dados(preco_teto_positiva)
    formatar_dados(preco_teto_negativa)


    return render_template("./painel/carteira_estudo.html",
                           acoes=acoes,
                           dividendo_recebidos=f"R$ {dividendo_recebidos:,.2f}",
                           rentabilidade=f"R$ {rentabilidade:,.2f}",
                           valor_atualizado=f"R$ {valor_atualizado:,.2f}",
                           valor_total_investido=f"R$ {valor_total_investido:,.2f}",
                           current_route=current_route,
                           preco_teto=preco_teto_dados,
                           preco_teto_positiva=preco_teto_positiva,
                           preco_teto_negativa=preco_teto_negativa)
