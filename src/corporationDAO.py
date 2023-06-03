from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from Corporation import Empresa

# Create the connection engine
engine = create_engine('mysql+mysqlconnector://root:ubermensch@localhost/db_green_world')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

#_____________________________GET COMPANIES_____________________________________________________________
# Query all records from the 'tbl_empresa_parceira' table

def bring_companies():
    status = True
    try:
        companies = session.query(Empresa).all()

        # Create an empty list to store company dictionaries
        company_list = []

        # Iterate over the companies and create a dictionary for each one
        for company in companies:
            company_dict = {
                'id': company.id,
                'cnpj': company.cnpj,
                'nome_fantasia': company.nome_fantasia,
                'telefone': company.telefone,
                'email': company.email,
                'id_administrador': company.id_administrador
            }

            # Add the dictionary to the current company list
            company_list.append(company_dict)

        # Close the session
        session.close()

        return company_list

    except Exception as e:
        status = False
        return status

#_________________________________________________UPDATE COMPANIES______________________________________
def update_company(company_id, new_nome_fantasia, new_telefone, new_cnpj, new_email):
    try:
        # Query the company by ID
        company = session.query(Empresa).filter(Empresa.id == company_id).first()

        # Check if the company was found
        if company:
            # Update the company attributes
            
            company.nome_fantasia = new_nome_fantasia
            company.telefone = new_telefone
            company.cnpj = new_cnpj
            company.email = new_email

            # Commit to save the changes to the database
            session.commit()

            status = True
            return status

    except Exception as e:
        status = False
        return status

#__________________________DELETE________________________________________________

def delete_company(company_id):
    try:
        # Query the company by ID
        company = session.query(Empresa).filter(Empresa.id == company_id).first()

        # Check if the company was found
        if company:
            # Remove the company from the session
            session.delete(company)

            # Commit to save the removal to the database
            session.commit()

            status = True
            return status

    except Exception as e:
        status = False
        return status

#_______________________________GET COMPANY BY ID_____________________________________________
def bring_company_by_id(company_id):
    status = True
    try:
        company = session.query(Empresa).filter(Empresa.id == company_id).first()

        if company is not None:
            company_data = {
                'id': company.id,
                'cnpj': company.cnpj,
                'nome_fantasia': company.nome_fantasia,
                'telefone': company.telefone,
                'email': company.email,
                'id_administrador': company.id_administrador
            }
            return company_data
        else:
            return None

    except Exception as e:
        status = False
        return status
    
#print(bring_company_by_id(15))
#________________________________________________________________________________________________

def insert_company(cnpj, nome_fantasia, telefone, email, id_administrador):
    try:
        # Cria uma nova instância da classe Empresa
        nova_empresa = Empresa(cnpj=cnpj, nome_fantasia=nome_fantasia, telefone=telefone, email=email, id_administrador=id_administrador)

        # Adiciona a nova empresa à sessão
        session.add(nova_empresa)

        # Commit para salvar a nova empresa no banco de dados
        session.commit()

        status = True
        return status

    except Exception as e:
        status = False
        return status

# Exemplo de uso da função insert_company
status = insert_company("12345678901234", "PETA", "123456789", "peta@abc.com", 1)
