# Controller/AtivosController.py

from Model import Ativos
from Repository.AtivosDAO import AtivosDAO

class AtivosController:
    def __init__(self):
        self.dao = AtivosDAO()
    
    def incluir(self, ativo):
        return self.dao.incluir(ativo)
    
    def alterar(self, ativo):
        return self.dao.alterar(ativo)
    
    def excluir(self, ativo_id):
        return self.dao.excluir(ativo_id)
    
    def buscar_ativo_por_setor(self, usuario_id, setor):
        return self.dao.buscar_ativo_por_setor(usuario_id, setor)
    
    def buscar_ativo_por_categoria(self, usuario_id):
        return self.dao.buscar_ativo_por_categoria(usuario_id)
    
    def todos_ativos_por_usuario(self, usuario_id):
        return self.dao.todos_ativos_por_usuario(usuario_id)