from dash import dcc, html  # Atualização: Dash agora inclui dcc e html diretamente
from dash.dependencies import Input, Output
import plotly.graph_objs as go  # É importante importar 'plotly.graph_objs' para criar os gráficos
import plotly.graph_objects as go
import plotly.express as px
from Controller.AtivosController import AtivosController
from flask_login import current_user

def layout_principal():
    return html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content')
    ])

def display_page(pathname):
    if pathname == '/dashboard/grafico-categoria':
        return dcc.Graph(id='grafico-categoria')
    elif pathname == '/dashboard/grafico-ativos':
        return dcc.Graph(id='grafico-ativos')
    elif pathname == '/dashboard/grafico-setor':
        return dcc.Graph(id='grafico-setor')
    elif pathname == '/dashboard/grafico-fundos':
        return dcc.Graph(id='grafico-fundos')
    elif pathname == '/dashboard/grafico-cotacao':
        return dcc.Graph(id='grafico-cotacao')
    elif pathname == '/dashboard/grafico-dividendo':
        return dcc.Graph(id='grafico-dividendo')
    else:
        return html.Div("404 - Página não encontrada")

# Função para atualizar o gráfico de categoria
def atualizar_grafico_categoria(id):  # Carteira por tipo de ativos
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
        font=dict(size=14, color='black', weight='bold'),
        margin=dict(t=20, b=20),
        showlegend=True,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',        
        height=390,
    )
    
    return fig

# Função para atualizar o gráfico de ativos
def atualizar_grafico_ativos(id):  # Carteira consolidada
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
        font=dict(size=11, color='black', weight='bold'),        
        margin=dict(t=20, b=20),
        showlegend=True,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',        
        height=400,
    )
    
    return fig

# Função para atualizar o gráfico de cotações
def atualizar_grafico_ativos_cotacao(id):  # Cotação atualizada dos ativos
    ativos_controller = AtivosController()
    usuario_id = current_user.id  # Pega o ID do usuário atual
    dados = ativos_controller.todos_ativos_por_usuario_atualizado(usuario_id)

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
        font=dict(size=11, color='black', weight='bold'),        
        margin=dict(t=20, b=20),
        showlegend=True,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',        
        height=400,
    )
    
    return fig

# Função para gerar o gráfico por setor na categoria "Ação"
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

# Função para gerar o gráfico por setor na categoria "FIIs"
def grafico_fundos(id):  # Gráfico de setores da categoria "FIIs"
    ativos_controller = AtivosController()
    usuario_id = current_user.id  # Pega o ID do usuário atual

    # Obtendo o valor investido por setor para a categoria "FIIs"
    setores_fiis = ativos_controller.valor_investido_por_setor_fiis(usuario_id)

    setores = list(setores_fiis.keys())
    valores = list(setores_fiis.values())

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


def grafico_dividendo(id):
    ativos_controller = AtivosController()
    usuario_id = current_user.id  # Pega o ID do usuário atual

    # Obtendo os dividendos por ativo
    setores_fiis = ativos_controller.dividendos_por_ativo(usuario_id)

    ativos = list(setores_fiis.keys())
    dividendos = list(setores_fiis.values())

    # Gerando uma paleta de cores única para cada ativo
    cores = px.colors.qualitative.Plotly  # Usando a paleta de cores 'Plotly' como exemplo
    cor_unica_para_cada_ativo = [cores[i % len(cores)] for i in range(len(ativos))]

    # Configurando o gráfico de barras
    fig = go.Figure(data=[go.Bar(
        x=ativos,
        y=dividendos,
        text=[f'R${d:,.2f}' for d in dividendos],  # Formatando os dividendos como moeda
        textposition='auto',
        marker=dict(color=cor_unica_para_cada_ativo),  # Atribuindo cores únicas
        hovertemplate='%{x}<br>R$%{y:,.2f}<extra></extra>',
        hoverlabel=dict(namelength=-1)
    )])

    fig.update_layout(
        font=dict(size=11, color='black', weight='bold'),
        margin=dict(t=20, b=20),
        showlegend=False,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        height=400,
        xaxis_title="Ativos",
        yaxis_title="Dividendos (R$)"
    )

    return fig

