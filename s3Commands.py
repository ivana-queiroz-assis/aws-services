import boto3

s3=boto3.resource('s3')
#List of buckets in s3 in my account.
for bucket in s3.buckets.all():
    print(bucket.name)