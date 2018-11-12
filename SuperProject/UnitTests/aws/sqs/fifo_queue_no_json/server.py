#!/usr/bin/python3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html
# https://stackoverflow.com/questions/37034308/aws-sqs-boto3-send-message-returns-dict-object-has-no-attribute-send-message

##For Deduplication error -- I change the configuration in AWS
# https://stackoverflow.com/questions/28111941/sqs-delivering-a-message-only-once

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
    
queue = sqs.get_queue_by_name(QueueName='SampleFifoQueue.fifo')
for attr in queue.attributes:
    print(attr)
print(queue.url)

#print("%s" % str(queue.attributes.get('CreatedTimestamp')))

print()
print()

client_sqs = boto3.client('sqs')
queue_url = client_sqs.get_queue_url(QueueName='SampleFifoQueue.fifo')

num_message = 0
while(True):
    message_string = 'Test' + str(num_message)
    
    #Send SQS message to SQS queue
    response = client_sqs.send_message(
        QueueUrl=queue_url['QueueUrl'],
        MessageBody=message_string,
        MessageGroupId='messageGroup1'
        )

    print('Message send response: {}'.format(response))
    print()
    time.sleep(20)
    num_message = num_message + 1
