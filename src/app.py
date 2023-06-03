# python -m venv venv
#.\venv\Scripts\activate

from flask import Flask,make_response, jsonify, request

from corporation_controller import all_companies, company_by_id,update_by_id,delete_company_by_id
app = Flask(__name__)

#__________________________________GET ALL CORPORATIONS___________________________________

@app.route("/allcorporations", methods=['GET'])
def bring_all_corporations():

    operarion_status,companies = all_companies()
    return make_response(
             jsonify(
                status = operarion_status,
                data = companies

            )
        )
#__________________________________BY ID ___________________________________

@app.route("/companiebyid", methods=['POST'])
def bring_corporation():

    comp_id =request.json['companie_id']

    operarion_status,companies = company_by_id(comp_id)

    return make_response(
             jsonify(
                status = operarion_status,
                data = companies
               
            )
        )

#__________________________________________________________________________________________

@app.route("/updatecompaniebyid", methods=['PUT'])
def update_corporation():

    comp_id =request.json['companie_id']
    new_nome_fantasia =request.json['companie_new_name']
    new_telefone =request.json['companie_new_phonne']
    new_cnpj =request.json['companie_cnpj']
    new_email =request.json['new_email']
    


    operarion_status,companies = update_by_id(comp_id, new_nome_fantasia, new_telefone, new_cnpj, new_email)

    return make_response(
             jsonify(
                status = operarion_status,
                data = companies
               
            )
        )

#________________________DELETE_____________________________________________________________

@app.route("/deletecompaniebyid", methods=['DELETE'])

def delete_corporation():

    comp_id =request.json['companie_id']

    status_code, b = delete_company_by_id(comp_id)

    return make_response(
             jsonify(
        
                status = status_code,
                data = b
               
            )
        )


app.run(debug=True,port=8080)
