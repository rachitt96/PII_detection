#This program will download the test data (stored in S3 bucket) to "data" folder. 

import boto3

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

try:
	s3_resource.Bucket('enronsamples').download_file('test_emails.tsv', 'data/aws_downloaded.tsv')
	print('Successfully downloaded the test dataset')

except Exception as exc:
	print(exc)
	



