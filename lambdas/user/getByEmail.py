import json
import logging
import os
import boto3

dynamodb = boto3.resource('dynamodb', os.environ['REGION'])

def handler(event, context):
    sessionId = event["pathParameters"]["userId"]

    table = dynamodb.Table(os.environ['USER_TABLE'])
    
    result = table.query(KeyConditionExpression=Key('userId').eq(sessionId))

    response = {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "content-type":"application/json",
        },
        'statusCode': 200,
        'body': json.dumps(result)
    }

    return response