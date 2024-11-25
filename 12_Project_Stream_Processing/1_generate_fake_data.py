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
def main():
    while True:
        data = generate_note_data()
        time.sleep(1)
        print(data)

if __name__ == "__main__":
    main()