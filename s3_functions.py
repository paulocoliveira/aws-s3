import boto3
import json
import os
from boto3.s3.transfer import TransferConfig
from progress_percentage import ProgressPercentage

def s3_client():
    s3 = boto3.client('s3')
    return s3

def s3_resource():
    s3 = boto3.resource('s3')
    return s3

def create_bucket(bucket_name, location):
    print(bucket_name)
    return s3_client().create_bucket(
        Bucket=bucket_name, 
        CreateBucketConfiguration={
            'LocationConstraint': location
        }
    )

def list_buckets():
    return s3_client().list_buckets()

def delete_bucket(bucket_name):
    return s3_client().delete_bucket(
        Bucket=bucket_name
    )

def create_bucket_policy(bucket_name):
    bucket_policy = {
        "Version":"2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:*"],
                "Resource": ["arn:aws:s3:::" + bucket_name + "/*"]
            }
        ]
    }

    policy_string = json.dumps(bucket_policy)
    return s3_client().put_bucket_policy(
        Bucket=bucket_name,
        Policy=policy_string
    )

def update_bucket_policy(bucket_name):
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement":[
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:DeleteObject",
                    "s3:GetObject",
                    "s3:PutObject"
                ],
                "Resource":"arn:aws:s3:::" + bucket_name + '/*'
            }
        ]
    }

    policy_string = json.dumps(bucket_policy)
    return s3_client().put_bucket_policy(
        Bucket=bucket_name,
        Policy = policy_string
    )

def get_bucket_policy(bucket_name):
    return s3_client().get_bucket_policy(Bucket=bucket_name)

def server_side_encrypt_bucket(bucket_name):
    return s3_client().put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            "Rules":[
                {
                    "ApplyServerSideEncryptionByDefault":{
                        "SSEAlgorithm": "AES256"
                    }
                }
            ]
        }
    )

def get_bucket_encryption(bucket_name):
    return s3_client().get_bucket_encryption(Bucket=bucket_name)

def upload_small_file(bucket_name, file_name):
    file_path = os.path.dirname(__file__) + "\\resources\\" + file_name
    return s3_client().upload_file(file_path, bucket_name, file_name)

def upload_large_file(bucket_name, file_name):
    config = TransferConfig(multipart_threshold=1024 * 25, max_concurrency=10,
                            multipart_chunksize=1024 * 25, use_threads=True)
    file_path = os.path.dirname(__file__) + "\\resources\\" + file_name
    key_path = "multipart_files/" + file_name
    s3_resource().meta.client.upload_file(file_path, bucket_name, key_path,
                                          ExtraArgs={"ACL": "public-read", "ContentType":"application/x-ms-installer"},
                                          Config=config,
                                          Callback=ProgressPercentage(file_path))

def read_object_from_bucket(bucket_name, file_name):
    return s3_client().get_object(
        Bucket=bucket_name,
        Key=file_name
    )

def version_bucket_files(bucket_name):
    s3_client().put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={
            "Status": "Enabled"
        }
    )

def put_lifecycle_policy(bucket_name):
    lifecycle_policy = {
        "Rules": [
            {
                "ID": "Move readme file to Glacier",
                "Prefix": "readme",
                "Status": "Enabled",
                "Transitions": [
                    {
                        "Date": "2019-01-01T00:00:00.000Z",
                        "StorageClass": "GLACIER"
                    }
                ]
            },
            {
                "ID": "Move old versions to Glacier",
                "Status": "Enabled",
                "Prefix": "",
                "NoncurrentVersionTransitions": [
                    {
                        "NoncurrentDays": 2,
                        "StorageClass": "GLACIER"
                    }
                ]
            }
        ]
    }

    s3_client().put_bucket_lifecycle_configuration(
        Bucket=bucket_name,
        LifecycleConfiguration=lifecycle_policy
    )