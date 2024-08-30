from Model.Preco_teto import Preco_teto
from Model import db
from sqlalchemy.orm import sessionmaker
import yfinance as yf

class Preco_TetoDAO:
    def __init__(self):
        self.Session = sessionmaker(bind=db.engine)
        
    def incluir(self, preco_teto):
        session = self.Session()
        try:
            session.add(preco_teto)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def alterar(self, preco_teto):
        session = self.Session()
        try:
            session.merge(preco_teto)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def excluir(self, preco_teto):
        session = self.Session()
        try:
            session.delete(preco_teto)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
        
    def buscar_preco_teto_por_usuario(self, usuario_id):
        session = self.Session()
        try:
            resultado = session.query(Preco_teto).filter_by(usuario_id=usuario_id).all()
            
            return resultado
        except Exception as e:
            raise e
        finally:
            session.close()

    
    def calcular_preco_teto_por_usuario(self, usuario_id):
        preco_teto_list = self.buscar_preco_teto_por_usuario(usuario_id)
        preco_teto_dict = {}
        
        for preco_teto in preco_teto_list:
            ticket = preco_teto.ticket
            preco_teto_calculado = preco_teto.media_recebido / preco_teto.media_dividendos
            
            
            try:
                ticker = yf.Ticker(ticket)
                history = ticker.history(period="1d")
                if not history.empty:
                    cotacao_atual = history['Close'].iloc[-1]
                    
                else:
                    cotacao_atual = 'N/A'
            except Exception as e:
                cotacao_atual = 'N/A'
            margem_de_seguranca = ((preco_teto_calculado - cotacao_atual) / cotacao_atual) * 100
            preco_teto.media_dividendos = preco_teto.media_dividendos * 100
            margem_pessoal = ((preco_teto.preco_pessoal - cotacao_atual) / cotacao_atual) *100
            
            preco_teto_dict[ticket] = {
                'preco_teto_calculado': preco_teto_calculado,
                'cotacao_atual': cotacao_atual,
                'media_dividendos': preco_teto.media_dividendos,
                'media_recebido': preco_teto.media_recebido,
                'preco_pessoal': preco_teto.preco_pessoal,
                'margem_de_seguranca': margem_de_seguranca,
                'margem_pessoal': margem_pessoal
            }
            
        
        return preco_teto_dict

