import logging
import os
import boto3
import json

from utils.createResponse import CreateResponse
from models.session import Session
dynamodb = boto3.resource('dynamodb', region_name=os.environ['REGION'])

def handler(event, context):
    data = json.loads(event["body"])

    table = dynamodb.Table(os.environ['SESSION_TABLE'])

    session = Session(**data)

    table.put_item(Item=session.__dict__)

    return CreateResponse(session.__dict__)
    