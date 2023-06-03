from corporationDAO import bring_companies

#_________________________________________ALL COMPANIES _______________________________

def all_companies():
    status = True
    try:
        
        companies = bring_companies()
        return companies
    
    except Exception as e:

        status = False
        return status

print(all_companies())
