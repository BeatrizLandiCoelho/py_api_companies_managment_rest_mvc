from corporationDAO import bring_companies,bring_company_by_id,delete_company
from tools import ERROR_DATA_NOT_FULLFILL,COMPANY_NOT_FOUND,COMPANIE_DELETED

def cheek_if_is_a_number(value):

    if isinstance(value, (int, float)):
        return True
    else: 
        return False

#_________________________________________ALL COMPANIES _______________________________

def all_companies():
    status = True
    try:
        
        companies = bring_companies()
        return companies
    
    except Exception as e:

        status = False
        return status

#___________________________________BY ID_______________________

def company_by_id(id):

    status = True

    if id != '' and cheek_if_is_a_number(id)== True: 
        
        try:    
            companie = bring_company_by_id(id)
            if companie != None:
                return companie
            elif companie == None:
                return COMPANY_NOT_FOUND
        
        except Exception as e:

            status = False
            return status
    else:
        return ERROR_DATA_NOT_FULLFILL
#print(company_by_id(15))
#________________________________________DELETE_____________________________________

def delete_company_by_id(id):
     
     status = True

     if id != '' and cheek_if_is_a_number(id)== True: 
        try:    
            companie = delete_company(id)
            return COMPANIE_DELETED
        
        except Exception as e:

            status = False
            return status
     else:
        return ERROR_DATA_NOT_FULLFILL

#________________________________________UPDATE_____________________________________
        
        

