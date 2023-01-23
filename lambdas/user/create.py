import logging
import os
import boto3
import json

from utils.createResponse import CreateResponse
from models.user import User
dynamodb = boto3.resource('dynamodb', region_name=os.environ['REGION'])

def handler(event, context):
    data = json.loads(event["body"])

    table = dynamodb.Table(os.environ['USER_TABLE'])

    user = User(**data)

    table.put_item(Item=user.__dict__)

    return CreateResponse(user.__dict__)
    