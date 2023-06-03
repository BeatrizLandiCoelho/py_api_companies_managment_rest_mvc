# python -m venv venv
#.\venv\Scripts\activate

from flask import Flask,make_response, jsonify, request

from corporation_controller import all_companies

app = Flask(__name__)

#__________________________________GET ALL CORPORATIONS___________________________________

@app.route("/allcorporations", methods=['GET'])
def bring_all_corporations():

    companies = all_companies()
    return make_response(
             jsonify(
                status = 200,
                dta = companies

            )
        )
#__________________________________POST A CORPORATION___________________________________


app.run(debug=True,port=8080)
