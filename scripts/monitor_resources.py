import boto3
import logging

logging.basicConfig(
    filename='../logs/automation.log',
    level=logging.INFO
)

try:
    s3 = boto3.client('s3')

    response = s3.list_buckets()

    print("\nAvailable Buckets:\n")

    for bucket in response['Buckets']:
        print(bucket['Name'])

    logging.info("Bucket list fetched successfully")

except Exception as e:
    print("Error:", e)
    logging.error(str(e))