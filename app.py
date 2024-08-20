from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import secrets
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask_session import Session

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
