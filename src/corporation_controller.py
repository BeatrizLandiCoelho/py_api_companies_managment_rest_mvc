from corporationDAO import bring_companies,bring_company_by_id,delete_company,update_company
from tools import ERROR_DATA_NOT_FULLFILL,COMPANY_NOT_FOUND,COMPANIE_DELETED,ERROR_INTERNAL

def cheek_if_is_a_number(value):

    if isinstance(value, (int, float)):
        return True
    else: 
        return False

def cheek_len(txt):
    quantidade_caracteres = len(txt)
    return quantidade_caracteres

#_________________________________________ALL COMPANIES _______________________________

def all_companies():
    status = True
    try:
        
        companies = bring_companies()
        return 200,companies 
    
    except Exception as e:

        
        return 500,ERROR_INTERNAL

#___________________________________BY ID_______________________

def company_by_id(id):

    id_int = int(id)

    if id_int != '' and cheek_if_is_a_number(id_int) == True: 
        
        try:    
            companie = bring_company_by_id(id_int)
            if companie != None:
                return 200, companie
            
            elif companie == None:
                return 404, COMPANY_NOT_FOUND
        
        except Exception as e:

           
            return 500, ERROR_INTERNAL
    else:
        return 400,ERROR_DATA_NOT_FULLFILL
    
#print(company_by_id("16"))
status, company = company_by_id("16")
#print(status)
#print(company)
#________________________________________DELETE_____________________________________

def delete_company_by_id(comp_id):
     
     id= int(comp_id)

     status = True

     if id != '' and cheek_if_is_a_number(id)== True: 
        try:    
            delete_company(id)
            return 200, COMPANIE_DELETED
        
        except Exception as e:

            return 500, ERROR_INTERNAL
     else:
        return 400, ERROR_DATA_NOT_FULLFILL

#delete_company_by_id(15)
#print(delete_company_by_id(15))
#________________________________________UPDATE_____________________________________
    
def update_by_id(comp_id, new_nome_fantasia, new_telefone, new_cnpj, new_email):

    id= int(comp_id)

    if (
        id != '' 
        and new_nome_fantasia != ''
        and new_telefone != ''
        and new_cnpj != ''
        and new_email !=''
        and cheek_len(new_telefone) < 10
        and cheek_if_is_a_number(id)== True
        ): 
        
        try:    
            companie = update_company(id, new_nome_fantasia, new_telefone, new_cnpj, new_email)
            if companie != None:
                status, company = company_by_id(id)
                return status, company
            
            elif companie == None:
                return 404, COMPANY_NOT_FOUND
        
        except Exception as e:

            return 500, ERROR_INTERNAL
    else:
        return 400, ERROR_DATA_NOT_FULLFILL
