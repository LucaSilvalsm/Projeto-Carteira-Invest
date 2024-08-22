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
    
    def soma_dividendos_recebidos(self, usuario_id):
        return self.dao.soma_dividendos_recebidos(usuario_id)
    
    def valor_total_investido(self, usuario_id):
        return self.dao.valor_total_investido(usuario_id)
    
    def ativos_por_categoria(self, categoria):
        return self.dao.ativos_por_categoria(categoria)
    def ativos_acao(self):
        return self.ativos_por_categoria("Ação")
    def ativos_fiis(self):
        return self.ativos_fiis("FIIs")
    def valor_investido_por_setor_acao(self, usuario_id):
        return self.dao.valor_investido_por_setor_acao(usuario_id)

    def valor_investido_por_setor_fiis(self, usuario_id):
        return self.dao.valor_investido_por_setor_fiis(usuario_id)
    def valor_investido_atualizado(self, usuario_id):
        return self.dao.valor_investido_atualizado(usuario_id)
    
    def atualizar_cotacoes(self, usuario_id):
        return self.dao.atualizar_cotacoes(usuario_id)