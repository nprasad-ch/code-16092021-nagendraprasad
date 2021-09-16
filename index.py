import json
import boto3
import os
client=boto3.client("s3")

def lambda_handler(event,context):
    sqs_message=event
    print(event)
    sns_content=event["Records"][0]["body"]
    print(sns_content)
    msg_body=sns_content
    client.put_object(Body=msg_body, Bucket=os.environ["bucket_name"], Key=f"data.txt")
    return None
