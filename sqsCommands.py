import boto3
def create_queue():
    # Get the service resource
    sqs = boto3.resource('sqs')
    queue = sqs.create_queue(QueueName='ivana-queue', Attributes={'DelaySeconds': '5'})
    # You can now access identifiers and attributes
    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))
    return queue.url

def send_message(queue_url):
    # Create SQS client
    sqs = boto3.client('sqs')
    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'John Grisham'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )
    print(response['MessageId'])

def receive_delete_message(queue_url):
    # Create SQS client
    sqs = boto3.client('sqs')
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
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
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    print('Received and deleted message: %s' % message)
# queue_url = create_queue()
# send_message('https://us-west-2.queue.amazonaws.com/831368754098/ivana-queue')
receive_delete_message('https://us-west-2.queue.amazonaws.com/831368754098/ivana-queue')