import logging
from flask_jwt_extended import create_access_token, decode_token


def encodeToken():

    try:
        token = create_access_token('ufg-br', expires_delta=False)
    except Exception as e:
        logging.error("Encoded Error", e)
        return "-1", 404
    if token:
        return token, 201
    else: 
        return None, 404

def decodeToken(token):
    try:
        decoded = decode_token(token)
        appId = decoded['sub']
        # logs.logger.info(appId)
        return appId
    except Exception as e:
        # logs.logger.info(e)
        return e
