import boto3

def create_s3_bucket(bucket_name, location):
    client = boto3.client('s3')
    response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': location},)
    print(response)
    return response

def upload_to_s3(file_path, bucket_name, key_name)
    client = boto3.client('s3')
    client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')