from s3_functions import create_s3_bucket, upload_to_s3
from random import randrange

my_bucket = "bucket-" + str(randrange(1000))
location = "us-east-2"
file_path_1 = 
file_key_1 = "view.jpg"
file_path_2 = 
file_key_2 = "text_file.txt"

create_s3_bucket(my_bucket, location)
upload_to_s3(my_bucket, file_path_1, file_key_1)
upload_to_s3(my_bucket, file_path_2, file_key_2)
