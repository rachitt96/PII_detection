import boto3

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

'''
for bucket in s3.buckets.all():
	print(bucket.name)
'''
'''
bucket_policies = s3_client.get_bucket_acl(Bucket = 'enronsamples')
print(bucket_policies)
'''

try:
	s3_resource.Bucket('enronsamples').download_file('test_emails.tsv', 'aws_downloaded.tsv')
except Exception as exc:
	print(exc)
	



