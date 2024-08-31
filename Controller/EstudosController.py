from Model.Estudos import Estudos
from Repository.EstudosDAO import EstudosDAO

class EstudosController():
    def __init__(self):
        self.dao = EstudosDAO()
        
    def incluir(self, estudo):
        return self.dao.incluir(estudo)
    
    def alterar(self, estudo):
        return self.dao.alterar(estudo)
    
    def excluir(self, estudo_id):
        return self.dao.excluir(estudo_id)
    
    def buscar_id_ativo_por_ticket(self, ticket_escolhido, usuario_id):
        return self.dao.buscar_id_ativo_por_ticket(ticket_escolhido, usuario_id)
    
    def buscar_preco_teto_por_usuario(self, usuario_id):
        return self.dao.buscar_preco_teto_por_usuario(usuario_id)
    
    def buscar_ativos_por_usuario(self, usuario_id):
        return self.dao.buscar_ativos_por_usuario(usuario_id)
    
    def calcular_preco_teto_por_usuario(self, usuario_id):
        return self.dao.calcular_preco_teto_por_usuario(usuario_id)
    
    def calcular_preco_teto_positiva_por_usuario(self, usuario_id):
        return self.dao.calcular_preco_teto_positiva_por_usuario(usuario_id)
    
    def calcular_preco_teto_negativa_por_usuario(self, usuario_id):
        return self.dao.calcular_preco_teto_negativa_por_usuario(usuario_id)
