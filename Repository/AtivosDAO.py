# Repository/AtivosDAO.py

from Model.Ativos import Ativos
from Model import db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import yfinance as yf  

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

    def ativos_por_categoria(self,usuario_id, categoria):
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
    
    def valor_investido_por_setor(self, usuario_id, categoria):
        session = self.Session()
        try:
            setores = session.query(Ativos.setor).filter(Ativos.usuario_id == usuario_id, Ativos.categoria == categoria).distinct().all()
            resultados = {}

            for setor, in setores:
                total_investido_setor = session.query(
                    func.sum(Ativos.quantidade * Ativos.preco_medio)
                ).filter(
                    Ativos.usuario_id == usuario_id,
                    Ativos.setor == setor,
                    Ativos.categoria == categoria
                ).scalar() or 0
                resultados[setor] = total_investido_setor

            return resultados
        finally:
            session.close()
    def valor_investido_atualizado(self, usuario_id):
        session = self.Session()
        try:
            # Busca todos os ativos do usuário
            ativos = session.query(Ativos).filter(Ativos.usuario_id == usuario_id).all()
            total_investido_atualizado = 0

            for ativo in ativos:
                # Verifica se o ativo pertence à categoria "Renda Fixa"
                if ativo.categoria == "Renda Fixa":
                    # Para "Renda Fixa", apenas soma o valor investido originalmente
                    valor_investido = ativo.quantidade * ativo.preco_medio
                else:
                    # Obtém a cotação atual do ticket usando yfinance
                    ticker = yf.Ticker(ativo.ticket_ativo)
                    historico = ticker.history(period='1d')

                    # Verifica se o histórico não está vazio
                    if not historico.empty:
                        cotacao_atual = historico['Close'].iloc[0]  # Usando iloc para acessar o primeiro valor
                        cotacao_atual = float(cotacao_atual)  # Converte np.float64 para float padrão do Python

                        # Calcula o valor investido com a cotação atualizada sem alterar o banco
                        valor_investido = ativo.quantidade * cotacao_atual
                    else:
                        print(f"Nenhuma cotação disponível para o ativo: {ativo.ticket_ativo}")
                        valor_investido = ativo.quantidade * ativo.preco_medio  # Caso não haja cotação atual, usa o preço médio

                # Soma o valor investido (atualizado ou original) ao total
                total_investido_atualizado += valor_investido

            return total_investido_atualizado

        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def ativos_acao(self):
        return self.ativos_por_categoria("Ação")

    def ativos_fiis(self):
        return self.ativos_por_categoria("FIIs")

    def valor_investido_por_setor_acao(self, usuario_id):
        return self.valor_investido_por_setor(usuario_id, "Ação")

    def valor_investido_por_setor_fiis(self, usuario_id):
        return self.valor_investido_por_setor(usuario_id, "FIIs")
    
    def atualizar_cotacoes(self, usuario_id):
        session = self.Session()
        try:
            # Busca todos os ativos do usuário
            ativos = session.query(Ativos).filter(Ativos.usuario_id == usuario_id).all()
            
            for ativo in ativos:
                # Busca a cotação atual usando yfinance
                ticker = yf.Ticker(ativo.ticket_ativo)
                cotacao_atual = ticker.history(period='1d')['Close'][0]
                
                # Atualiza o preço médio do ativo com a cotação atual
                ativo.preco_medio = cotacao_atual
                
                session.merge(ativo)
            
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
