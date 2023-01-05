import logging
import os
import boto3

from boto3.dynamodb.conditions import Key
from utils.createResponse import CreateResponse

dynamodb = boto3.resource('dynamodb', os.environ['REGION'])

def handler(event, context):
    email = event["queryStringParameters"]["email"]

    table = dynamodb.Table(os.environ['USER_TABLE'])
    
    result = table.query(
        IndexName='user_email-index',
        KeyConditionExpression=Key('email').eq(email)
        )

    print(result)

    return CreateResponse(result["Items"])