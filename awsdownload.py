import os
import time
import sys
import boto3
import settings

# datetime object containing current date and time



session = boto3.Session(
    aws_access_key_id=settings.AWS_SERVER_PUBLIC_KEY,
    aws_secret_access_key=settings.AWS_SERVER_SECRET_KEY)

s3 = session.resource('s3')

bucket = s3.Bucket('is-dev-tee-media-streams')

#prefix = sys.argv[0]
prefix = 'nfl/season2021/TEE21_1.1_Run2/int/nfl20_intel_2021010313/76/vcamconfig/auto/'
files = bucket.objects.filter(Prefix=prefix)
files = [obj.key for obj in sorted(files, key=lambda x: x.last_modified,
    reverse=True)][0:2]





timestr = time.strftime("%Y%m%d-%H%M%S")
print(timestr)
cwd = os.getcwd()
file_name = cwd + "\\vcamConfig_" + timestr + ".json"
print(file_name)
for file in files:
    if 'vcamConfigMapping' not in file:
        bucket.download_file(file, file_name)
