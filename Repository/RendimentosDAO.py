from Model.Rendimentos import Rendimentos
from Model.Ativos import Ativos  
from Model import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import extract
from collections import defaultdict

class RendimentosDAO():
    def __init__(self):
        self.Session = sessionmaker(bind=db.engine)
    
    def incluir(self, rendimentos):
        session = self.Session()
        try:
            session.add(rendimentos)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            
    def alterar(self, rendimento):
        session = self.Session()
        try:
            session.merge(rendimento)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def excluir(self, rendimentos_id):
        session = self.Session()
        try:
            rendimentos = session.query(Rendimentos).filter(Rendimentos.id == rendimentos_id).first()
            if rendimentos:
                session.delete(rendimentos)
                session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            
    from sqlalchemy import func

    def soma_dividendos_totais(self, usuario_id):
        session = self.Session()
        try:
            # Soma dos dividendos na tabela Rendimentos
            soma_rendimentos = session.query(func.sum(Rendimentos.valor_recebido)).filter(Rendimentos.usuario_id == usuario_id).scalar() or 0

            # Retorna a soma total dos dividendos
            return soma_rendimentos
            
        finally:
            session.close()

    
    def dividendos_por_ativo(self, usuario_id):
        session = self.Session()
        try:
            # Query para somar os valores recebidos na tabela Rendimentos, agrupados por nome_ativos
            dividendos_rendimentos = session.query(
                Rendimentos.nome_ativos,
                func.sum(Rendimentos.valor_recebido).label('total_dividendos_rendimentos')
            ).filter(Rendimentos.usuario_id == usuario_id).group_by(Rendimentos.nome_ativos).all()

            # Combina os resultados em um dicionário
            resultado = {}

            for nome_ativos, total_dividendos_rendimentos in dividendos_rendimentos:
                # Converte nome_ativos para string se necessário (isso pode depender do tipo da coluna)
                nome_ativos = str(nome_ativos)
                resultado[nome_ativos] = total_dividendos_rendimentos

            return resultado

        finally:
            session.close()
    def dividendos_por_mes(self, usuario_id):
        session = self.Session()
        try:
            # Query para somar dividendos na tabela Rendimentos, agrupados por mês e ano
            dividendos_mes = session.query(
                extract('year', Rendimentos.data_dividendo).label('ano'),
                extract('month', Rendimentos.data_dividendo).label('mes'),
                func.sum(Rendimentos.valor_recebido).label('total_dividendos')
            ).filter(Rendimentos.usuario_id == usuario_id).group_by(
                extract('year', Rendimentos.data_dividendo), 
                extract('month', Rendimentos.data_dividendo)
            ).all()

            # Combina os resultados em um dicionário
            resultado = {}

            for ano, mes, total_dividendos in dividendos_mes:
                # Converte ano e mes para inteiros
                ano = int(ano)
                mes = int(mes)
                chave = f"{ano}-{mes:02d}"
                resultado[chave] = resultado.get(chave, 0) + total_dividendos

            return resultado

        finally:
            session.close()
    def dividendos_por_ano(self, usuario_id):
        session = self.Session()
        try:
            # Query para somar dividendos na tabela Rendimentos, agrupados por ano
            dividendos_ano = session.query(
                extract('year', Rendimentos.data_dividendo).label('ano'),
                func.sum(Rendimentos.valor_recebido).label('total_dividendos')
            ).filter(Rendimentos.usuario_id == usuario_id).group_by(
                extract('year', Rendimentos.data_dividendo)
            ).all()

            # Combina os resultados em um dicionário
            resultado = {}

            for ano, total_dividendos in dividendos_ano:
                # Converte ano para inteiro e adiciona ao resultado
                ano = int(ano)
                resultado[ano] = total_dividendos

            return resultado

        finally:
            session.close()
    def dividendos_totais_por_ativo(self, usuario_id):
        session = self.Session()
        try:
            # Query para somar os dividendos por nome do ativo na tabela Rendimentos
            dividendos_por_ativo = session.query(
                Rendimentos.nome_ativos,
                func.sum(Rendimentos.valor_recebido).label('total_dividendos')
            ).filter(Rendimentos.usuario_id == usuario_id).group_by(Rendimentos.nome_ativos).all()

            # Combina os resultados em um dicionário
            resultado = {nome_ativo: total_dividendos for nome_ativo, total_dividendos in dividendos_por_ativo}

            return resultado

        finally:
            session.close()