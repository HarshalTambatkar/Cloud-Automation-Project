import boto3
import logging
import os

# Project root path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Log file path
LOG_FILE = os.path.join(BASE_DIR, "logs", "automation.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    s3 = boto3.client('s3')

    bucket_name = "harshal-cloud-automation-bucket"

    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'eu-north-1'
            }
        )

        print("Bucket created successfully")
        logging.info(f"Bucket {bucket_name} created successfully")

    except s3.exceptions.BucketAlreadyOwnedByYou:
        print("Bucket already exists")
        logging.info(f"Bucket {bucket_name} already exists")

except Exception as e:
    print("Error:", e)
    logging.error(f"Error occurred: {str(e)}")