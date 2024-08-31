from Repository.Preco_tetoDAO import Preco_TetoDAO
from Model.Preco_teto import Preco_teto



class PrecoController():
    def __init__(self):
        self.dao = Preco_TetoDAO()
        
    def incluir(self, preco_teto):
        return self.dao.incluir(preco_teto)
    
    def alterar(self, preco_teto):
        return self.dao.alterar(preco_teto)
    
    def excluir(self,preco_teto):
        return self.dao.excluir(preco_teto)
    
    def calcular_preco_teto_por_usuario(self, usuario_id):
        return self.dao.calcular_preco_teto_por_usuario(usuario_id)
    
    def buscar_preco_teto_por_usuario(self, usuario_id):
        return self.dao.buscar_preco_teto_por_usuario(usuario_id)
    
    def calcular_preco_teto_positiva(self, usuario_id):
        return self.dao.calcular_preco_teto_positiva(usuario_id)
    
    def calcular_preco_teto_negativo(self, usuario_id):
        return self.dao.calcular_preco_teto_negativo(usuario_id)