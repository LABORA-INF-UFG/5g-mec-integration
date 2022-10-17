from flask import request, Blueprint, Flask, json

imc_calc = Blueprint('imc_calc', '__name__', url_prefix='/imc-calc')

@imc_calc.route('/', methods=['POST'])
def imcCalc():
    imc_result = 0
    information = request.get_json()
    response = calculate_imc(information)
    return response


def calculate_imc(information):
    peso = information["peso"]
    altura = information["altura"]
    if peso != None and altura != None:
        imc = peso/(altura * altura)

        if (imc > 18, 4) and (imc < 25):
            classificacao = "Normal"
        elif (imc > 25) and (imc <= 29, 9):
            classificacao = "Sobrepeso"
        elif (imc > 30) and (imc < 39, 9):
            classificacao = "Obesidade"
        else:
            classificacao = "Obsidade Grave"
        imc_result = {
            "classificacao": classificacao,
            "imc": imc,
            "peso": peso,
            "altura": altura,
        }
        result_json = json.dumps(imc_result)
        response = Flask.response_class(response=result_json, status=201)
        return response
    else:
        response = Flask.response_class(response="Dados incompletos", status=404)
        return 