import json
import logging
import os
import boto3

from boto3.dynamodb.conditions import Key
from utils.decimalEncoder import DecimalEncoder

dynamodb = boto3.resource('dynamodb', os.environ['REGION'])

def handler(event, context):
    sessionId = event["pathParameters"]["userId"]

    table = dynamodb.Table(os.environ['SESSION_TABLE'])
    
    result = table.query(
        IndexName='session_userId-index',
        KeyConditionExpression=Key('userId').eq(sessionId)
        )

    print(result["Items"])

    response = {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "content-type":"application/json",
        },
        'statusCode': 200,
        'body': json.dumps(result["Items"], cls=DecimalEncoder)
    }

    return response