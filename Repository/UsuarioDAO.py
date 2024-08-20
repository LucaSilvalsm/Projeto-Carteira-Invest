from Model import db
from Model.Usuario import Usuario
from sqlalchemy.orm import sessionmaker

class UsuarioDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=db.engine)
    
    def incluir(self, usuario):
        session = self.Session()
        try:
            session.add(usuario)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def alterar(self, usuario):
        session = self.Session()
        try:
            usuario_atual = session.query(Usuario).filter(Usuario.id == usuario.id).first()
            if usuario_atual:
                usuario_atual.nome = usuario.nome
                usuario_atual.sobrenome = usuario.sobrenome
                usuario_atual.email = usuario.email
                usuario_atual.cpf = usuario.cpf
                if usuario.senha:
                    usuario_atual.set_senha(usuario.senha)
                session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def obter_por_id(self, id):
        session = self.Session()
        try:
            return session.query(Usuario).filter(Usuario.id == id).first()
        finally:
            session.close()
    
    def obter_por_email(self, email):
        session = self.Session()
        try:
            return session.query(Usuario).filter(Usuario.email == email).first()
        finally:
            session.close()
    
    def obter_por_cpf(self, cpf):
        session = self.Session()
        try:
            return session.query(Usuario).filter(Usuario.cpf == cpf).first()
        finally:
            session.close()
