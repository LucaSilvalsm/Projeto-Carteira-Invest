import bcrypt
from Model import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    
    ativos = db.relationship('Ativos', backref='usuario', lazy=True)
    
    def __init__(self, nome, sobrenome, email, senha, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.set_senha(senha)  # Use o método para definir a senha
        self.cpf = cpf
    
    def set_senha(self, senha):
        # Cria o hash da senha
        self.senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def verificar_senha(self, senha):
        # Verifica a senha fornecida com o hash armazenado
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha.encode('utf-8'))

    def get_id(self):
        return self.id
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False