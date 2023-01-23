import json
from utils.decimalEncoder import DecimalEncoder

def CreateResponse(body):
    response = {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers" : "*",
            "content-type":"application/json",
        },
        'statusCode': 200,
        'body': json.dumps(body, cls=DecimalEncoder)
    }

    return response
