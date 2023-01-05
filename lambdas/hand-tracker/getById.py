import json
import logging
import os
import boto3

from utils.decimalEncoder import DecimalEncoder

dynamodb = boto3.resource('dynamodb', os.environ['REGION'])

def handler(event, context):
    id = event["pathParameters"]["id"]

    table = dynamodb.Table(os.environ['HAND_TRACKER_TABLE'])
    
    result = table.get_item(Key={'id': id})

    print(result)

    response = {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "content-type":"application/json",
        },
        'statusCode': 200,
        'body': json.dumps(result["Item"], cls=DecimalEncoder)
    }

    return response