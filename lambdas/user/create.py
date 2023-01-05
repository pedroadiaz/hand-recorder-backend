import logging
import os
from datetime import datetime
import uuid
import boto3

from utils.createResponse import CreateResponse
dynamodb = boto3.resource('dynamodb', region_name=os.environ['REGION'])

def handler(event, context):
    data = json.loads(event["body"])

    timestamp = str(datetime.now())

    table = dynamodb.Table(os.environ['USER_TABLE'])

    id = str(uuid.uuid4())

    if "id" in data:
        id = data["id"]

    item = {
        'id': id,
        'email': data['email'],
        'created': timestamp
    }

    table.put_item(Item=item)

    response = {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Credentials": True,
            "Access-Control-Allow-Headers" : "*",
            "content-type":"application/json",
        },
        'statusCode': 200,
        'body': json.dumps(item)
    }

    return CreateResponse(item)
    