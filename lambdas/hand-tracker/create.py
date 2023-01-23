import json
import logging
import os

dynamodb = boto3.resource('dynamodb')

from utils.createResponse import CreateResponse
from models.hand import Hand

def handler(event, context):
    data = json.loads(event["body"])

    hand = Hand(**data)

    table = dynamodb.Table(os.environ['HAND_TRACKER_TABLE'])

    table.put_item(Item=hand.__dict__)

    return CreateResponse(hand.__dict__)
    