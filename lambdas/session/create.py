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

    return CreateResponse(item)
    