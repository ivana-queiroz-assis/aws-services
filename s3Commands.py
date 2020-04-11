import boto3
import botocore

def create_bucket():
    s3 = boto3.resource('s3')
    s3.create_bucket(Bucket='ivana-ptyhon-bucket3', CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'})
    
def list_buckets():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

def upload_files():
    s3 = boto3.resource('s3')
    s3.Object('ivana-ptyhon-bucket2', 'hello.txt').put(Body=open('/home/ivana/Documents/aws-python/first.txt', 'rb'))

def accessing_bucket():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('ivana-ptyhon-bucket3')
    exists = True
    try:
        s3.meta.client.head_bucket(Bucket='ivana-ptyhon-bucket3')
    except botocore.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            print('Não existe bucket!!!')
            exists = False
accessing_bucket()