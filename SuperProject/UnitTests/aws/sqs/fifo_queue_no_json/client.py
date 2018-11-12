#!/usr/bin/python3

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/sqs.html
# https://aws.amazon.com/blogs/developer/using-python-and-amazon-sqs-fifo-queues-to-preserve-message-sequencing/

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
print(queue_url['QueueUrl'])
print()

num_message = 0
while(True):
    
    # Receive message from SQS queue
    response = queue.receive_messages()
    message = response[0]
    message.delete()
    print('Received and automatically deleted message: %s' % message.body)
    print()
    time.sleep(30)
