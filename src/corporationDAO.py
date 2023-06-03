from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Corporation import Empresa

# Cria a engine de conexão
engine = create_engine('mysql+mysqlconnector://root:ubermensch@localhost/db_green_world')


# Cria uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

#__________________________________________________________________________________________
# Consulta todos os registros da tabela 'tbl_empresa_parceira

def bring_companies():
    status = True
    try:
        empresas = session.query(Empresa).all()

        # Cria uma lista vazia para armazenar os dicionários de empresas
        lista_empresas = []

        # Itera sobre as empresas e cria um dicionário para cada uma
        for empresa in empresas:
            dict_empresa = {
                'id': empresa.id,
                'cnpj': empresa.cnpj,
                'nome_fantasia': empresa.nome_fantasia,
                'telefone': empresa.telefone,
                'email': empresa.email,
                'id_administrador': empresa.id_administrador
            }

            # Adiciona o dicionário à lista de empresas atual
            lista_empresas.append(dict_empresa)

        # Adiciona a lista atual de empresas à lista de listas de empresas
       
        # Imprime a lista de dicionários de empresas
        
            for dict_empresa in lista_empresas:
                dict_empresa

        # Fecha a sessão
        session.close()

        return lista_empresas

#camila vamo casa
    except Exception as e:
        status = False
        return status
#_______________________________________________________________________________________





