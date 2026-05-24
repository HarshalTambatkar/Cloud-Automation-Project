import boto3
import logging

# Logging setup
logging.basicConfig(
    filename='../logs/automation.log',
    level=logging.INFO
)

try:
    s3 = boto3.client('s3')

    bucket_name = "harshal-cloud-automation-bucket"

    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-north-1'
        }
    )

    print("Bucket created successfully")
    logging.info(f"Bucket {bucket_name} created successfully")

except Exception as e:
    print("Error:", e)
    logging.error(str(e))