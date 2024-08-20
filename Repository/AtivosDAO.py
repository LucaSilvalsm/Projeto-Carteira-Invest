# Controller/page_ativos.py

from Model.Ativos import Ativos
from Model import db
from sqlalchemy.orm import sessionmaker

class AtivosDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=db.engine)
    
    def incluir(self, ativo):
        session = self.Session()
        try:
            session.add(ativo)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def alterar(self, ativo):
        session = self.Session()
        try:
            session.merge(ativo)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    def excluir(self, ativo_id):
        session = self.Session()
        try:
            ativo = session.query(Ativos).filter(Ativos.id == ativo_id).first()
            if ativo:
                session.delete(ativo)
                session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def buscar_ativos_por_usuario(self, usuario_id):
        session = self.Session()
        try:
            return session.query(Ativos).filter(Ativos.usuario_id == usuario_id).all()
        finally:
            session.close()

    def buscar_ativo_por_setor(self, usuario_id, setor):
        session = self.Session()
        try:
            return session.query(Ativos).filter(Ativos.usuario_id == usuario_id, Ativos.setor == setor).first()
        finally:
            session.close()

    def buscar_ativo_por_categoria(self, usuario_id):
        session = self.Session()  # Corrigida a indentação
        try:
            categorias = ["Acao", "FIIs", "ETF", "Renda Fixa"]
            resultados = {}

            for categoria in categorias:
                ativos = session.query(Ativos).filter(Ativos.usuario_id == usuario_id, Ativos.categoria == categoria).all()
                total_categoria = sum(ativo.quantidade * ativo.preco_medio for ativo in ativos)
                resultados[categoria] = total_categoria
            
            return resultados
        
        finally:
            session.close()

    def todos_ativos_por_usuario(self, usuario_id):
        session = self.Session()
        try:
            ativos = session.query(Ativos).filter(Ativos.usuario_id == usuario_id).all()
            resultado = {}
            for ativo in ativos:
                valor_total = ativo.quantidade * ativo.preco_medio
                resultado[ativo.ticket_ativo] = valor_total
            return resultado
        finally:
            session.close()
