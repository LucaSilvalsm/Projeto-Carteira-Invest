from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from Model.Usuario import Usuario
from Model.Ativos import Ativos
from Model.Rendimentos import Rendimentos 
from Model.Preco_teto import Preco_teto