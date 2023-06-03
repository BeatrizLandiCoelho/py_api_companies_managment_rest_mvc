
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Cria uma classe base para as classes de modelo
Base = declarative_base()

# Define uma classe de modelo para a tabela 'tbl_empresa_parceira'
class Empresa(Base):
    __tablename__ = 'tbl_empresa_parceira'
    id = Column(Integer, primary_key=True)
    cnpj = Column(String(18))
    nome_fantasia = Column(String(150))
    telefone = Column(String(15))
    email = Column(String(256))
    id_administrador = Column(Integer)