from Model import db

class Rendimentos(db.Model):
    __tablename__ = 'rendimentos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_dividendo = db.Column(db.Date, nullable=False)
    valor_recebido = db.Column(db.Float, nullable=False)
    ativo_id = db.Column(db.Integer, db.ForeignKey('ativos.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    nome_ativos = db.Column(db.String(100), nullable=False)

    

    def __init__(self, data_dividendo, valor_recebido, ativo_id, usuario_id, nome_ativos):
        self.data_dividendo = data_dividendo
        self.valor_recebido = valor_recebido
        self.ativo_id = ativo_id
        self.usuario_id = usuario_id
        self.nome_ativos = nome_ativos




