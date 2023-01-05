import json
import logging
import os
import boto3

from utils.createResponse import CreateResponse

dynamodb = boto3.resource('dynamodb', os.environ['REGION'])

def handler(event, context):
    id = event["pathParameters"]["id"]

    table = dynamodb.Table(os.environ['HAND_TRACKER_TABLE'])
    
    result = table.get_item(Key={'id': id})

    print(result)

    return CreateResponse(result["Item"])