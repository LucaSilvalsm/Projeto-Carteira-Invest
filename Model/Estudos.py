from Model import db 

class Estudos(db.Model):
    __tablename__ = 'estudos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    ticket_escolhido = db.Column(db.String(100), nullable=False)    
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    media_rendimentos = db.Column(db.Float, nullable=False)
    media_recebido = db.Column(db.Float, nullable=False)
    preco_pessoal = db.Column(db.Float, nullable=False)

    def __init__(self, ticket_escolhido, usuario_id, media_rendimentos, media_recebido, preco_pessoal):
        self.ticket_escolhido = ticket_escolhido        
        self.usuario_id = usuario_id
        self.media_rendimentos = media_rendimentos
        self.media_recebido = media_recebido
        self.preco_pessoal = preco_pessoal
