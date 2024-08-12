from Model import db


class Ativos(db.Model):
    __tablename__ = 'ativos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_ativo = db.Column(db.String(100), nullable=False)
    ticket_ativo = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    setor = db.Column(db.String(100), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    preco_medio = db.Column(db.Float, nullable=False)
    dividendos = db.Column(db.Float, nullable=False)
    preco_pessoal = db.Column(db.Float, nullable=False)
    
    def __init__(self, nome_ativo, ticket_ativo, categoria, setor, usuario_id, quantidade, preco_medio, dividendos, preco_pessoal):
        self.id = id
        self.nome_ativo = nome_ativo
        self.ticket_ativo = ticket_ativo
        self.categoria = categoria
        self.setor = setor
        self.usuario_id = usuario_id
        self.quantidade = quantidade
        self.preco_medio = preco_medio
        self.dividendos = dividendos
        self.preco_pessoal = preco_pessoal
        