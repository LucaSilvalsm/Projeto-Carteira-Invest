from Model.Estudos import Estudos  # Corrigido o import do módulo
from Model import db
from sqlalchemy.orm import sessionmaker
import yfinance as yf

class EstudosDAO:
    
    def __init__(self):
        self.Session = sessionmaker(bind=db.engine)
    
    def incluir(self, estudos):
        session = self.Session()
        try:
            session.add(estudos)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def listar(self):
        session = self.Session()
        try:
            return session.query(Estudos).all()
        finally:
            session.close()
    
    def alterar(self, estudos):
        session = self.Session()
        try:
            session.merge(estudos)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    def excluir(self, estudo_id):
        session = self.Session()
        try:
            estudo = session.query(Estudos).get(estudo_id)  # Buscando a instância do objeto
            if estudo:
                session.delete(estudo)
                session.commit()
            else:
                raise ValueError(f"Estudo com ID {estudo_id} não encontrado.")
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def buscar_id_ativo_por_ticket(self, ticket_escolhido, usuario_id):
        session = self.Session()
        try:
            # Verifique se o ticket_escolhido e usuario_id são válidos
            if not ticket_escolhido:
                print(f"Ticket vazio fornecido para UsuarioID={usuario_id}")
                return None

            if not usuario_id:
                print("UsuarioID não fornecido")
                return None
            
            print(f"Buscando ativo para Ticket='{ticket_escolhido}' e UsuarioID={usuario_id}")  # Depuração
            
            # Execute a consulta para buscar o ativo
            ativo = session.query(Estudos).filter(
                Estudos.ticket_escolhido == ticket_escolhido,
                Estudos.usuario_id == usuario_id
            ).first()  # Use .first() para obter um único resultado

            # Se encontrado, imprime e retorna o ID
            if ativo:
                print(f"Ativo encontrado: ID={ativo.id}, Ticket={ticket_escolhido}, UsuarioID={usuario_id}")
                return ativo.id
            else:
                print(f"Nenhum ativo encontrado para Ticket='{ticket_escolhido}' e UsuarioID={usuario_id}")
                return None
        except Exception as e:
            # Captura e exibe qualquer exceção que ocorrer
            print(f"Erro ao buscar ativo: {e}")
            return None
        finally:
            session.close()





    
    def buscar_preco_teto_por_usuario(self, usuario_id):
        session = self.Session()
        try:
            return session.query(Estudos).filter_by(usuario_id=usuario_id).all()
        except Exception as e:
            raise e
        finally:
            session.close()
            
    def buscar_ativos_por_usuario(self, usuario_id):
        session = self.Session()
        try:
            return session.query(Estudos).filter_by(usuario_id=usuario_id).all()
        except Exception as e:
            raise e
        finally:
            session.close()


    def calcular_preco_teto_por_usuario(self, usuario_id):
        estudo_list = self.buscar_preco_teto_por_usuario(usuario_id)
        estudo_dict = {}
        
        for estudo in estudo_list:
            ticket_escolhido = estudo.ticket_escolhido  # Corrigido para uso de 'estudo'
            preco_teto_calculado = estudo.media_recebido / estudo.media_rendimentos
            
            try:
                ticker = yf.Ticker(ticket_escolhido)
                history = ticker.history(period="1d")
                if not history.empty:
                    cotacao_atual = history['Close'].iloc[-1]
                else:
                    cotacao_atual = 'N/A'
            except Exception as e:
                cotacao_atual = 'N/A'
            
            if cotacao_atual != 'N/A':
                cotacao_atual = float(cotacao_atual)  # Convertendo para float
            
                margem_de_seguranca = ((preco_teto_calculado - cotacao_atual) / cotacao_atual) * 100
                estudo_dict[ticket_escolhido] = {
                    'preco_teto_calculado': preco_teto_calculado,
                    'cotacao_atual': cotacao_atual,
                    'media_dividendos': estudo.media_rendimentos * 100,  # Corrigido para 'estudo'
                    'media_recebido': estudo.media_recebido,
                    'preco_pessoal': estudo.preco_pessoal,
                    'margem_de_seguranca': margem_de_seguranca,
                    'margem_pessoal': ((estudo.preco_pessoal - cotacao_atual) / cotacao_atual) * 100
                }
        
        return estudo_dict
    def calcular_preco_teto_positiva_por_usuario(self, usuario_id):
        estudo_list = self.buscar_preco_teto_por_usuario(usuario_id)
        estudo_dict = {}
        
        for estudo in estudo_list:
            ticket_escolhido = estudo.ticket_escolhido
            preco_teto_calculado = estudo.media_recebido / estudo.media_rendimentos
            
            try:
                ticker = yf.Ticker(ticket_escolhido)
                history = ticker.history(period="1d")
                if not history.empty:
                    cotacao_atual = history['Close'].iloc[-1]
                else:
                    cotacao_atual = 'N/A'
            except Exception as e:
                cotacao_atual = 'N/A'
            
            if cotacao_atual != 'N/A':
                cotacao_atual = float(cotacao_atual)
                margem_de_seguranca = ((preco_teto_calculado - cotacao_atual) / cotacao_atual) * 100
                
                if margem_de_seguranca > 0:
                    estudo_dict[ticket_escolhido] = {
                        'preco_teto_calculado': preco_teto_calculado,
                        'cotacao_atual': cotacao_atual,
                        'media_dividendos': estudo.media_rendimentos * 100,
                        'media_recebido': estudo.media_recebido,
                        'preco_pessoal': estudo.preco_pessoal,
                        'margem_de_seguranca': margem_de_seguranca,
                        'margem_pessoal': ((estudo.preco_pessoal - cotacao_atual) / cotacao_atual) * 100
                    }
        
        return estudo_dict

    def calcular_preco_teto_negativa_por_usuario(self, usuario_id):
        estudo_list = self.buscar_preco_teto_por_usuario(usuario_id)
        estudo_dict = {}
        
        for estudo in estudo_list:
            ticket_escolhido = estudo.ticket_escolhido
            preco_teto_calculado = estudo.media_recebido / estudo.media_rendimentos
            
            try:
                ticker = yf.Ticker(ticket_escolhido)
                history = ticker.history(period="1d")
                if not history.empty:
                    cotacao_atual = history['Close'].iloc[-1]
                else:
                    cotacao_atual = 'N/A'
            except Exception as e:
                cotacao_atual = 'N/A'
            
            if cotacao_atual != 'N/A':
                cotacao_atual = float(cotacao_atual)
                margem_de_seguranca = ((preco_teto_calculado - cotacao_atual) / cotacao_atual) * 100
                
                if margem_de_seguranca < 0:
                    estudo_dict[ticket_escolhido] = {
                        'preco_teto_calculado': preco_teto_calculado,
                        'cotacao_atual': cotacao_atual,
                        'media_dividendos': estudo.media_rendimentos * 100,
                        'media_recebido': estudo.media_recebido,
                        'preco_pessoal': estudo.preco_pessoal,
                        'margem_de_seguranca': margem_de_seguranca,
                        'margem_pessoal': ((estudo.preco_pessoal - cotacao_atual) / cotacao_atual) * 100
                    }
        
        return estudo_dict


