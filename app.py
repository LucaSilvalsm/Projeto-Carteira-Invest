from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager, UserMixin, current_user
from flask_session import Session
from Controller.AtivosController import AtivosController

# Importando o Dash
from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

# Importando blueprints
from Controller.page_controller import page_bp
from Controller.page_usuario import user_bp
from Controller.page_ativos import ativos_bp

# Importar a instância do banco de dados
from Model import db, Usuario
from Model.config import DATABASE

app = Flask(__name__)
app.secret_key = secrets.token_hex(24)

DB_URL = f"postgresql://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuração da sessão
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configuração do Dash
dash_app = Dash(__name__, server=app, url_base_pathname='/dashboard/')

# Layout principal do Dash com dcc.Location
dash_app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Callback para renderizar a página correta
@dash_app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard/grafico-categoria':
        return dcc.Graph(id='grafico-categoria')
    elif pathname == '/dashboard/grafico-ativos':
        return dcc.Graph(id='grafico-ativos')
    elif pathname == '/dashboard/grafico-setor':
        return dcc.Graph(id='grafico-setor')
    elif pathname == '/dashboard/grafico-fundos':
        return dcc.Graph(id='grafico-fundos')
    else:
        return html.Div("404 - Página não encontrada")

# Callback para atualizar o gráfico de categoria
@dash_app.callback(
    Output('grafico-categoria', 'figure'),
    [Input('grafico-categoria', 'id')]
)
def atualizar_grafico_categoria(id): #Carteira Por tipo de ativos
    ativos_controller = AtivosController()
    usuario_id = current_user.id  # Pega o ID do usuário atual
    dados = ativos_controller.buscar_ativo_por_categoria(usuario_id)

    categorias = list(dados.keys())
    valores = list(dados.values())

    # Configurando o gráfico de pizza
    fig = go.Figure(data=[go.Pie(
        labels=categorias, 
        values=valores,
        textinfo='label+percent',
        insidetextorientation='radial',
        marker=dict(line=dict(color='#000000', width=2)),
        hovertemplate='%{label}<br>R$%{value:,.2f}<br>%{percent}<extra></extra>',
        hoverlabel=dict(namelength=-1)
    )])

    fig.update_layout(
        font=dict(size=14, color='black',weight='bold'),
        margin=dict(t=20, b=20),
        showlegend=True,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',        
        height=390,
    )
    
    return fig

# Callback para atualizar o gráfico de ativos
@dash_app.callback(
    Output('grafico-ativos', 'figure'),
    [Input('grafico-ativos', 'id')]
)
def atualizar_grafico_ativos(id): #Carteira Consolidada
    ativos_controller = AtivosController()
    usuario_id = current_user.id  # Pega o ID do usuário atual
    dados = ativos_controller.todos_ativos_por_usuario(usuario_id)

    tickets = list(dados.keys())
    valores = list(dados.values())

    # Configurando o gráfico de pizza
    fig = go.Figure(data=[go.Pie(
        labels=tickets,
        values=valores,
        textinfo='label+percent',
        insidetextorientation='radial',
        marker=dict(line=dict(color='#000000', width=2)),
        hovertemplate='%{label}<br>R$%{value:,.2f}<br>%{percent}<extra></extra>',
        hoverlabel=dict(namelength=-1)
    )])

    fig.update_layout(
        font=dict(size=11, color='black',weight='bold'),        
        margin=dict(t=20, b=20),
        showlegend=True,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',        
        height=400,
        
    )
    
    return fig

@dash_app.callback(
    Output('grafico-setor', 'figure'),
    [Input('grafico-setor', 'id')]
)
def grafico_setor(id):  # Gráfico de setores da categoria "Ação"
    ativos_controller = AtivosController()
    usuario_id = current_user.id  # Pega o ID do usuário atual

    # Obtendo o valor investido por setor para a categoria "Ação"
    setores_acao = ativos_controller.valor_investido_por_setor_acao(usuario_id)

    setores = list(setores_acao.keys())
    valores = list(setores_acao.values())

    # Configurando o gráfico de pizza
    fig = go.Figure(data=[go.Pie(
        labels=setores,
        values=valores,
        textinfo='label+percent',
        insidetextorientation='radial',
        marker=dict(line=dict(color='#000000', width=2)),
        hovertemplate='%{label}<br>R$%{value:,.2f}<br>%{percent}<extra></extra>',
        hoverlabel=dict(namelength=-1)
    )])

    fig.update_layout(
        font=dict(size=11, color='black', weight='bold'),
        margin=dict(t=20, b=20),
        showlegend=True,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',        
        height=400,
    )
    
    return fig

@dash_app.callback(
    Output('grafico-fundos', 'figure'),
    [Input('grafico-fundos', 'id')]
)
def grafico_fundos(id):  # Gráfico de setores da categoria "Ação"
    ativos_controller = AtivosController()
    
    usuario_id = current_user.id  # Pega o ID do usuário atual
    # Obtendo o valor investido por setor para a categoria "Ação"
    setores_acao = ativos_controller.valor_investido_por_setor_fiis(usuario_id)

    setores = list(setores_acao.keys())
    valores = list(setores_acao.values())

    # Configurando o gráfico de pizza
    fig = go.Figure(data=[go.Pie(
        labels=setores,
        values=valores,
        textinfo='label+percent',
        insidetextorientation='radial',
        marker=dict(line=dict(color='#000000', width=2)),
        hovertemplate='%{label}<br>R$%{value:,.2f}<br>%{percent}<extra></extra>',
        hoverlabel=dict(namelength=-1)
    )])

    fig.update_layout(
        font=dict(size=11, color='black', weight='bold'),
        margin=dict(t=20, b=20),
        showlegend=True,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',        
        height=400,
    )
    
    return fig



# Inicializar o banco de dados
db.init_app(app)
app.register_blueprint(page_bp)
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(ativos_bp, url_prefix='/ativos')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user_bp.login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Usuario, user_id)

if __name__ == '__main__':
    with app.app_context():
        print("Criando tabelas no banco de dados...")
        db.create_all()
        print("Tabelas criadas com sucesso.")
    
    # Execução do aplicativo Flask
    app.run(debug=True)
