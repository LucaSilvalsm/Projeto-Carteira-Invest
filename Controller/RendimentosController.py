# Controller/RendimentosController.py

from Model.Rendimentos import Rendimentos
from Repository.RendimentosDAO import RendimentosDAO

class RendimentosController:
    def __init__(self):
        self.dao = RendimentosDAO()
    
    def   incluir(self, rendimentos):
        return self.dao.incluir(rendimentos)
    
    def alterar(self, rendimento):
        return self.dao.alterar(rendimento)
    
    def excluir(self, rendimentos_id):
        return self.dao.excluir(rendimentos_id)

    def soma_dividendos_totais(self, usuario_id):
        return self.dao.soma_dividendos_totais(usuario_id)
    
    def dividendos_por_ativo_com_rendimentos(self, usuario_id):
        return self.dao.dividendos_por_ativo_com_rendimentos(usuario_id)
    
    def dividendos_por_ativo(self, usuario_id):
        return self.dao.dividendos_por_ativo(usuario_id)
    
    def dividendos_por_mes(self, usuario_id):
        return self.dao.dividendos_por_mes(usuario_id)
    
    def dividendos_por_ano(self, usuario_id):
        return self.dao.dividendos_por_ano(usuario_id)
    
    def dividendos_totais_por_ativo(self, usuario_id):
        return self.dao.dividendos_totais_por_ativo(usuario_id)