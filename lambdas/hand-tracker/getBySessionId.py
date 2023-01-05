import logging
import os
import boto3

from utils.createResponse import CreateResponse
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', os.environ['REGION'])

def handler(event, context):
    sessionId = event["pathParameters"]["sessionId"]

    table = dynamodb.Table(os.environ['HAND_TRACKER_TABLE'])
    
    result = table.query(
        IndexName='handTracker_session-index',
        KeyConditionExpression=Key('sessionId').eq(sessionId)
        )

    print(result)

    return CreateResponse(result["Items"])