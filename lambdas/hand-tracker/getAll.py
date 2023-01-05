import logging
import os
import boto3

from utils.createResponse import CreateResponse

dynamodb = boto3.resource('dynamodb', os.environ['REGION'])

def handler(event, context):
    table = dynamodb.Table(os.environ['HAND_TRACKER_TABLE'])
    
    result = table.scan()

    print(result)

    return CreateResponse(result["Items"])