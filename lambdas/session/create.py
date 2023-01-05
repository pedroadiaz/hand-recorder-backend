import json
import logging
import os
from datetime import datetime
import uuid
import boto3

dynamodb = boto3.resource('dynamodb', region_name=os.environ['REGION'])

def handler(event, context):
    data = json.loads(event["body"])

    timestamp = str(datetime.now())

    table = dynamodb.Table(os.environ['SESSION_TABLE'])

    id = str(uuid.uuid4())

    if "id" in data:
        id = data["id"]

    item = {
        'id': id,
        'userId': data['userId'],
        'stackSize': data['stackSize'],
        'location': data['location'],
        'smallBlind': data['smallBlind'],
        'bigBlind': data['bigBlind'],
        'cashOutAmount': data['cashOutAmount'],
        'created': timestamp
    }

    table.put_item(Item=item)

    response = {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "content-type":"application/json",
        },
        'statusCode': 200,
        'body': json.dumps(item)
    }

    return response
    