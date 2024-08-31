# Controller/UsuarioController.py

from Model import Usuario
from Repository.UsuarioDAO import UsuarioDAO

class UsuarioController:
    def __init__(self):
        self.dao = UsuarioDAO()
    
    def incluir(self, usuario):
        return self.dao.incluir(usuario)
    
    def alterar(self, usuario):
        return self.dao.alterar(usuario)
    
    def excluir(self, usuario_id):
        return self.dao.excluir(usuario_id)
    
    def buscar_por_id(self, usuario_id):
        return self.dao.obter_por_id(usuario_id)
    
    def buscar_por_email(self, email):
        return self.dao.obter_por_email(email)
    
    def buscar_por_cpf(self, cpf):
        return self.dao.obter_por_cpf(cpf)
    
    def obter_nome_usuario(self,usuario_id):
        return self.dao.obter_nome_usuario(usuario_id)
