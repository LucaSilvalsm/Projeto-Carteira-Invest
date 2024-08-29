from dash import dcc, html  # Atualização: Dash agora inclui dcc e html diretamente
from dash.dependencies import Input, Output
import plotly.graph_objs as go  # É importante importar 'plotly.graph_objs' para criar os gráficos
import plotly.graph_objects as go
import plotly.express as px
from Controller.AtivosController import AtivosController
from Controller.RendimentosController import RendimentosController 
from flask_login import current_user
from collections import defaultdict
import locale
import calendar


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
    elif pathname == '/dashboard/grafico-dividendos-mes':
        return dcc.Graph(id='grafico-dividendos-mes')
    elif pathname == '/dashboard/grafico-dividendos-por-ano':
        return dcc.Graph(id='grafico-dividendos-por-ano')
    else:
        return html.Div("404 - Página não encontrada")

# Função para atualizar o gráfico de categoria
def atualizar_grafico_categoria(id):  # Carteira por tipo de ativos
    ativos_controller = AtivosController()
    usuario_id = current_user.id  # Pega o ID do usuário atual
    dados = ativos_controller.buscar_ativo_por_categoria_atualizado(usuario_id)

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
    
    usuario_id = current_user.id  # Pega o ID do usuário atual
    rendimentosController = RendimentosController()

    # Obtendo os dividendos por ativo
    setores_fiis = rendimentosController.dividendos_totais_por_ativo(usuario_id)

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
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        height=400,
        xaxis_title="Ativos",
        yaxis_title="Dividendos (R$)"
    )

    return fig


def grafico_dividendos_por_mes(id):
    rendimentosController = RendimentosController()
    usuario_id = current_user.id  # Pega o ID do usuário atual

    # Definindo o local para português
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

    # Obtendo os dividendos por mês
    dividendos_por_mes = rendimentosController.dividendos_por_mes(usuario_id)

    # Organizando os dados para o gráfico
    dados_por_mes_ano = defaultdict(lambda: defaultdict(float))

    for chave, valor in dividendos_por_mes.items():
        ano, mes = chave.split('-')
        dados_por_mes_ano[mes][ano] += valor

    # Preparando os dados para o gráfico
    meses_numeros = sorted(dados_por_mes_ano.keys())
    meses_abreviados = [calendar.month_abbr[int(mes_num)].capitalize() for mes_num in meses_numeros]
    anos = sorted(set(ano for ano_dict in dados_por_mes_ano.values() for ano in ano_dict.keys()))

    data = []
    for ano in anos:
        valores_ano = [dados_por_mes_ano[mes].get(ano, 0) for mes in meses_numeros]
        data.append(go.Bar(
            name=str(ano), 
            x=meses_abreviados, 
            y=valores_ano,
            text=[f'R${valor:,.2f}' for valor in valores_ano],  # Valores recebidos
            hovertemplate='%{x}<br>R$%{y:,.2f}<extra></extra>',
            textposition='auto'  # Exibe o valor automaticamente no topo
        ))

    # Configurando o gráfico de barras
    fig = go.Figure(data=data)

    fig.update_layout(
              
        
        xaxis_title='Mês',
        showlegend=True,
        yaxis_title='Dividendos (R$)',
        font=dict(size=11, color='black', weight='bold'),
        margin=dict(t=40, b=40),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        height=400,
    )

    return fig
 # Atualize para o nome correto do seu módulo

def grafico_dividendos_por_ano(id):
    rendimentosController = RendimentosController()
    usuario_id = current_user.id  # Pega o ID do usuário atual

    # Definindo o local para português
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

    # Obtendo os dividendos por ano
    dividendos_por_ano = rendimentosController.dividendos_por_ano(usuario_id)

    # Preparando os dados para o gráfico
    anos = sorted(dividendos_por_ano.keys())
    valores = [dividendos_por_ano[ano] for ano in anos]

    # Definindo cores diferentes para cada ano
    cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']  # Adapte conforme necessário

    # Criando o gráfico de barras horizontais
    fig = go.Figure(data=[go.Bar(
        x=valores,  # Valores no eixo X
        y=anos,     # Anos no eixo Y
        text=[f'R${valor:,.2f}' for valor in valores],  # Formatando os dividendos como moeda
        textposition='auto',
        marker=dict(color=cores),  # Atribui cores diferentes para cada ano
        orientation='h',  # Define a orientação das barras para horizontal
        hovertemplate='Ano: %{y}<br>Total: R$%{x:,.2f}<extra></extra>'  # Exibe o ano e o valor no tooltip
    )])

    # Atualizando o layout do gráfico
    fig.update_layout(
        xaxis_title='DIVIDENDOS (R$)',
        yaxis_title='ANO',
        font=dict(size=11, color='black', weight='bold'),
        margin=dict(t=40, b=40),
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        height=400,
        yaxis=dict(
            tickmode='linear',  # Define o modo de ticks para linear
            dtick=1,  # Define o intervalo dos ticks do eixo Y para 1
        ),
        xaxis=dict(
            tickprefix='R$',  # Adiciona o prefixo 'R$' aos ticks do eixo X
            tickformat=',.2f'  # Formata os ticks do eixo X para mostrar 2 casas decimais
        )
    )

    return fig