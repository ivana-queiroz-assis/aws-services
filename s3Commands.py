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

def deleting_keys_and_bucket():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('ivana-ptyhon-bucket2')
    for key in bucket.objects.all():
        print('Deletando o arquivo: ' + str(key))
        key.delete()
    print('Now i can delete the bucket: ' + str(bucket.name))
    bucket.delete()

def iteration_keys_buckets():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            print(key.key)
def get_access_control_list():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('elasticbeanstalk-us-east-1-831368754098')
    acl = bucket.Acl()
    for grant in acl.grants:
        print(str(grant))
def manage_cors_bucket():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('s3-lifecycle-ivana')
    cors = bucket.Cors()
    config = {
        'CORSRules': [
            {
                'AllowedMethods': ['GET'],
                'AllowedOrigins': ['*']
            }
        ]
    }
    cors.put(CORSConfiguration=config)
    cors.delete()
manage_cors_bucket()