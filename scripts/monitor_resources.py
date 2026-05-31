import boto3
import logging
import os
import json

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

LOG_FILE = os.path.join(
    BASE_DIR,
    "logs",
    "automation.log"
)

DATA_FILE = os.path.join(
    BASE_DIR,
    "outputs",
    "buckets.json"
)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:

    s3 = boto3.client("s3")

    response = s3.list_buckets()

    current_buckets = [
        bucket["Name"]
        for bucket in response["Buckets"]
    ]

    print("\nCurrent Buckets:\n")

    for bucket in current_buckets:
        print(bucket)

    previous_buckets=[]

    if os.path.exists(DATA_FILE):

        with open(DATA_FILE,"r") as file:

            try:
                previous_buckets=json.load(file)
            except:
                previous_buckets=[]

    new_buckets=set(current_buckets)-set(previous_buckets)

    deleted_buckets=set(previous_buckets)-set(current_buckets)

    for bucket in new_buckets:

        print(f"\nNEW BUCKET CREATED: {bucket}")

        logging.info(
            f"New bucket created: {bucket}"
        )

    for bucket in deleted_buckets:

        print(f"\nBUCKET DELETED: {bucket}")

        logging.info(
            f"Bucket deleted: {bucket}"
        )

    if not new_buckets and not deleted_buckets:

        print("\nNo changes detected")

        logging.info(
            "No bucket changes detected"
        )

    with open(DATA_FILE,"w") as file:

        json.dump(
            current_buckets,
            file
        )

except Exception as e:

    print("Error:",e)

    logging.error(
        f"Error occurred: {str(e)}"
    )