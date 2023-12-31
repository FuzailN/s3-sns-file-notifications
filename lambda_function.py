import json
import boto3

client = boto3.client('sns')

def lambda_handler(event, context):
    #print(json.dumps(event))
    EventName = event['Records'][0]['eventName']
    BucketName = event['Records'][0]['s3']['bucket']['name']
    ObjectName = event['Records'][0]['s3']['object']['key']
    
    
    response = client.publish(
    TopicArn='arn:aws:sns:us-east-1:594790630367:SNSTopic',
    Message='The triggered event is {}.The bucket name is {}. and, the file name is {}'.format(EventName, BucketName, ObjectName),
    Subject='upload-notification',
 
    MessageStructure='string',
    MessageAttributes={
        'String': {
            'DataType': 'String',
            'StringValue': 'String'
        }
            
    },
)