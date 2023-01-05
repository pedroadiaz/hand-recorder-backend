import logging
import os
import boto3

from boto3.dynamodb.conditions import Key
from utils.createResponse import CreateResponse

dynamodb = boto3.resource('dynamodb', os.environ['REGION'])

def handler(event, context):
    sessionId = event["pathParameters"]["userId"]

    table = dynamodb.Table(os.environ['SESSION_TABLE'])
    
    result = table.query(
        IndexName='session_userId-index',
        KeyConditionExpression=Key('userId').eq(sessionId)
        )

    print(result["Items"])

    return CreateResponse(result["Items"])