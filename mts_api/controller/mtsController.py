import logging

import connexion
from flask import Blueprint, Response, json, current_app as app, jsonify

# import logs
from models import MtsSessionInfo

mtsController = Blueprint('mtsController', 'mtsController', url_prefix='/mtsController')


@mtsController.route('', methods=['GET'])
def mts_capability_info_get():
    """Retrieve the MTS capability information
    Used to query information about the MTS information. Typically used in the &#39;Get MTS service Info from the MTS Service&#39; procedure as described in clause 6.2.6. # noqa: E501
    :rtype: MtsCapabilityInfo
    """
    dados = {
        "mtsAccessInfo": [
            {
                "accessId": 0,
                "accessType": 6,
                "metered": 1
            },
            {
                "accessId": 0,
                "accessType": 6,
                "metered": 1
            }
        ],
        "mtsMode": [
            5,
            5
        ],
        "timeStamp": {
            "nanoSeconds": 5,
            "seconds": 2
        }
    }
    headers = {
        'Accept': 'application/json',
    }
    response = Response(response=json.dumps(dados), status=201, headers=headers)
    return response


@mtsController.route('', methods=['POST'])
def mts_session_post():
    headers = {
        'Accept': 'application/json',
    }
    if connexion.request.is_json:
        mts_session_info = MtsSessionInfo.from_dict(connexion.request.get_json())
        token, idSession, code = encodeToken(mts_session_info)
        if code == 201:
            finalResponse = {
                'token': token,
                'idSession': idSession,
            }
            response = Response(response=finalResponse, status=code, headers=headers)

    else:
        response = Response(response='Fail', status=501, headers=headers)

    return response

@mtsController.route('', methods=['DELETE'])
def mts_session_delete():
    headers = {
        'Accept': 'application/json',
    }
    try:
        idSession = connexion.request.get_data()
    except Exception as e:
        logging.Logger.error(e)
        # logging.Logger.error(mensagem)

    # response = Response(response=mensagem, status=code, headers=headers)
    return "response", 500