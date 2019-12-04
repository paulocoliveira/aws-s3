from s3_functions import create_bucket, create_bucket_policy, list_buckets, upload_small_file, delete_bucket, get_bucket_policy, get_bucket_encryption, update_bucket_policy, server_side_encrypt_bucket, upload_large_file, read_object_from_bucket, version_bucket_files, put_lifecycle_policy
from random import randrange

my_bucket = "bucket-" + str(randrange(1000))
location = "us-east-2"
file_name_1 = "text_file.txt"
file_name_2 = "microsoft_teams_installer.exe"

print(create_bucket(my_bucket, location))
print(create_bucket_policy(my_bucket))
print(list_buckets())
print(version_bucket_files(my_bucket))
print(upload_small_file(my_bucket, file_name_1))
print(upload_small_file(my_bucket, file_name_1))
print(get_bucket_policy(my_bucket))
print(update_bucket_policy(my_bucket))
print(server_side_encrypt_bucket(my_bucket))
print(get_bucket_encryption(my_bucket))
print(upload_large_file(my_bucket, file_name_2))
print(read_object_from_bucket(my_bucket, file_name_1))
print(put_lifecycle_policy(my_bucket))
print(delete_bucket(my_bucket))