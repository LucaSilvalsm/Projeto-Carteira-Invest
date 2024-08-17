from Model import db
from Model.Usuario import Usuario
from sqlalchemy.orm import Session
from sqlalchemy import update

class UsuarioDAO:
    def __init__(self):
        self.Session = Session(bind=db.engine)
    
    def incluir(self, usuario):
        self.Session.add(usuario)
        self.Session.commit()
    
    def alterar(self, usuario):
        self.Session.execute(update(Usuario).where(Usuario.id == usuario.id).values
                    (nome=usuario.nome, sobrenome=usuario.sobrenome, 
                    email=usuario.email,
                    senha=usuario.senha, 
                    cpf=usuario.cpf))
        self.Session.commit()
    def obter_por_id(self, id):
        return self.Session.query(Usuario).filter(Usuario.id == id).first()
    
    def obter_por_email(self, email):
        return self.Session.query(Usuario).filter(Usuario.email == email).first()
    
    def close(self):
        self.Session.close()