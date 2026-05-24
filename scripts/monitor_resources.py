import boto3
import logging
import os

# Create absolute path for project directory
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
    # Connect to AWS S3
    s3 = boto3.client('s3')

    # Fetch bucket list
    response = s3.list_buckets()

    print("\nAvailable Buckets:\n")

    for bucket in response['Buckets']:
        print(bucket['Name'])

    logging.info("Bucket list fetched successfully")

except Exception as e:
    print("Error:", e)
    logging.error(f"Error occurred: {str(e)}")