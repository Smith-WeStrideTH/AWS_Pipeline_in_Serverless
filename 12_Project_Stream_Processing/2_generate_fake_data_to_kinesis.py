from faker import Faker
import json
import string
import boto3
from datetime import datetime, timedelta
import time
import random

def generate_note_data():
    Faker.seed(0)
    fake= Faker("th-TH")
    return {
        "user_id": fake.uuid4(),
        "timestamp": datetime.now().timestamp(),
        "company": fake.company(),
        "job": "Temperature",
        "user_name": "IoT-Device",
        "Temperature": round(random.uniform(23.0,45.0),2),
        "expires": (datetime.now() + timedelta(seconds=600)).timestamp()
    }
def send_data_to_kinesis(data):
    kinesis_client = boto3.client('kinesis', region_name='us-east-1')#update if needed
    partition_key = 'p1'
    stream_name = 'TemperatureSensor'
    try :
        response = kinesis_client.put_record(
            Data=json.dumps(data).encode('utf-8'),
            PartitionKey=partition_key,
            StreamName=stream_name
        )
        print(f"Send data to Kinesis {data}")
    except Exception as e:
        print(f"Error sending data {e}")


def main():
    while True:
        data = generate_note_data()
        send_data_to_kinesis(data)
        time.sleep(1)
        # print(data)
if __name__ == "__main__":
    main()