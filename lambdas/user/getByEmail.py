import json
import logging
import os
import boto3

from boto3.dynamodb.conditions import Key
from utils.decimalEncoder import DecimalEncoder

dynamodb = boto3.resource('dynamodb', os.environ['REGION'])

def handler(event, context):
    email = event["queryStringParameters"]["email"]

    table = dynamodb.Table(os.environ['USER_TABLE'])
    
    result = table.query(
        IndexName='user_email-index',
        KeyConditionExpression=Key('email').eq(email)
        )

    print(result)

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