from flask import Blueprint, render_template, flash, redirect, url_for, session,request
from Model.Usuario import Usuario
from Model.Ativos import Ativos
from Model.config import DATABASE
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine





page_bp = Blueprint('page_bp', __name__)
DB_URL = f"postgresql://{DATABASE['username']}:{DATABASE['password']}@{DATABASE['host']}:{DATABASE['port']}/{DATABASE['database']}"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

@page_bp.route('/')
def index():
   
    return render_template("index.html")

@page_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@page_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template("cadastro.html")