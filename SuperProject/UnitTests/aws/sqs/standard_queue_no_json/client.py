#!/usr/bin/python3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html

import sys
import time
import json

import boto3

#getting general information
sqs = boto3.resource('sqs')

num = 0
for queue in sqs.queues.all():    
    print('queue', num, ' : {}'.format(queue))
    print (queue.url)
    num = num + 1
    
queue = sqs.get_queue_by_name(QueueName='SampleQueue')
for attr in queue.attributes:
    print(attr)
print(queue.url)

#print("%s" % str(queue.attributes.get('CreatedTimestamp')))

print()
print()

client_sqs = boto3.client('sqs')
queue_url = client_sqs.get_queue_url(QueueName='SampleQueue')
print(queue_url['QueueUrl'])
print()

num_message = 0
while(True):
    
    # Receive message from SQS queue
    response = client_sqs.receive_message(
        QueueUrl=queue_url['QueueUrl'],
        AttributeNames=[
            'SentTimestamp'
            ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
            ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
        )
    
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']
    
    # Delete received message from queue
    client_sqs.delete_message(
        QueueUrl=queue_url['QueueUrl'],
        ReceiptHandle=receipt_handle
        )
    print('Received and deleted message: %s' % message)
    print()
    time.sleep(30)
