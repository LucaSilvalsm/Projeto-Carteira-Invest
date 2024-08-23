from flask import Flask,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager
from flask_session import Session

from dash import Dash
from dash.dependencies import Input, Output
import graficos as graficos
 # This is correct


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

# Layout principal do Dash
dash_app.layout = graficos.layout_principal()


# Callbacks do Dash
dash_app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])(graficos.display_page)
dash_app.callback(Output('grafico-categoria', 'figure'), [Input('grafico-categoria', 'id')])(graficos.atualizar_grafico_categoria)
dash_app.callback(Output('grafico-ativos', 'figure'), [Input('grafico-ativos', 'id')])(graficos.atualizar_grafico_ativos)
dash_app.callback(Output('grafico-cotacao', 'figure'), [Input('grafico-cotacao', 'id')])(graficos.atualizar_grafico_ativos_cotacao)
dash_app.callback(Output('grafico-setor', 'figure'), [Input('grafico-setor', 'id')])(graficos.grafico_setor)
dash_app.callback(Output('grafico-fundos', 'figure'), [Input('grafico-fundos', 'id')])(graficos.grafico_fundos)
dash_app.callback(Output('grafico-dividendo', 'figure'), [Input('grafico-dividendo', 'id')])(graficos.grafico_dividendo)





# Inicializar o banco de dados
db.init_app(app)
app.register_blueprint(page_bp)
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(ativos_bp, url_prefix='/ativos')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = None  # Desativa a mensagem padrão

@login_manager.unauthorized_handler
def unauthorized():
    flash('Necessário estar logado para acessar esta página.','error')
    return redirect(url_for('page_bp.login'))
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
