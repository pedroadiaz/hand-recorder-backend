import json
import logging
import os
from datetime import datetime
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')

def handler(event, context):
    data = json.loads(event["body"])

    timestamp = str(datetime.now())

    table = dynamodb.Table(os.environ['HAND_TRACKER_TABLE'])

    item = {
        'id': str(uuid.uuid4()),
        'sessionId': data['sessionid'],
        'stackSize': data['stackSize'],
        'position': data['position'],
        'holecards': data['holeCards'],
        'preFlopNotes': data['preFlopNotes'],
        'flopCards': data['flopCards'],
        'flopNotes': data['flopNotes'],
        'turnCard': data['turnCard'],
        'turnNotes': data['turnNotes'],
        'riverCard': data['riverCard'],
        'riverNotes': data['riverNotes'],
        'otherNotes': data['otherNotes'],
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
    