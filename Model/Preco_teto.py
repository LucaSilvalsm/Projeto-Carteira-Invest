from Model import db

class Preco_teto(db.Model):
    __tablename__ = 'preco_teto'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket = db.Column(db.String(100), nullable=False)
    ativo_id = db.Column(db.Integer, db.ForeignKey('ativos.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    media_dividendos = db.Column(db.Float, nullable=False)
    media_recebido = db.Column(db.Float, nullable=False)
    preco_pessoal = db.Column(db.Float, nullable=False)

   

    def __init__(self, ticket, ativo_id, usuario_id, media_dividendos, media_recebido, preco_pessoal):
        self.ticket = ticket
        self.ativo_id = ativo_id
        self.usuario_id = usuario_id
        self.media_dividendos = media_dividendos
        self.media_recebido = media_recebido
        self.preco_pessoal = preco_pessoal
