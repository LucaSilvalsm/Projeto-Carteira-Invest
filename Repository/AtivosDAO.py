# Repository/AtivosDAO.py

from Model.Ativos import Ativos
from Model import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

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
        session = self.Session()
        try:
            categorias = ["Ação", "FIIs", "ETF", "Renda Fixa"]
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

    def soma_dividendos_recebidos(self, usuario_id):
        session = self.Session()
        try:
            return session.query(func.sum(Ativos.dividendos)).filter(Ativos.usuario_id == usuario_id).scalar() or 0
        finally:
            session.close()
    
    def valor_total_investido(self, usuario_id):
        session = self.Session()
        try:
            ativos = session.query(Ativos).filter(Ativos.usuario_id == usuario_id).all()
            total_investido = sum(ativo.quantidade * ativo.preco_medio for ativo in ativos)
            return total_investido
        finally:
            session.close()

    def ativos_por_categoria(self, categoria):
        session = self.Session()
        try:
            ativos = session.query(Ativos).filter(Ativos.categoria == categoria).all()
            resultado = {}
            for ativo in ativos:
                valor_total = ativo.quantidade * ativo.preco_medio
                resultado[ativo.ticket_ativo] = valor_total
            return resultado
        finally:
            session.close()
    
    def valor_investido_por_setor(self, categoria):
        session = self.Session()
        try:
            setores = session.query(Ativos.setor).filter(Ativos.categoria == categoria).distinct().all()
            resultados = {}

            for setor, in setores:
                total_investido_setor = session.query(
                    func.sum(Ativos.quantidade * Ativos.preco_medio)
                ).filter(
                    Ativos.setor == setor,
                    Ativos.categoria == categoria
                ).scalar() or 0
                resultados[setor] = total_investido_setor

            return resultados
        finally:
            session.close()


    def ativos_acao(self):
        return self.ativos_por_categoria("Ação")

    def ativos_fiis(self):
        return self.ativos_por_categoria("FIIs")

    def valor_investido_por_setor_acao(self):
        return self.valor_investido_por_setor("Ação")

    def valor_investido_por_setor_fiis(self):
        return self.valor_investido_por_setor("FIIs")
