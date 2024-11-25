import boto3
import datetime
import time

import boto3.resources

def process_image_meta(images):
    original =None
    thumbnail= None
    for image in images:
        for key, value in image.items():
            if key == 'original':
                original = f"{value['bucket']}|{value['key']}"
            elif key == 'resized':
                thumbnail = f"{value['bucket']}|{value['key']}"
            
    return {
        "original": original,
        "thumbnail": thumbnail
    }


def lambda_handler(event,context):
    try:
        images = process_image_meta(event['results']['images'])
        dynamodb= boto3.resource('dynamodb')
        table = dynamodb.Table('thumbnails')

        item ={
            "original": images['original'],
            "thumbnail": images['thumbnail'],
            "timestamp":  datetime.date.fromtimestamp(time.time()).isoformat()
        }
        table.put_item(Item=item)
        return True
    except Exception as e:
        print(e)
        return False

event = {
    "results":{
        "images":[
            {
                "original":{
                    "bucket": "my-bucket",
                    "key": 'image.png'
                },
                "resized":{
                    "bucket": "my-destination",
                    "key" : "image_resized.png"
                }
            }
        ]
    }
}

lambda_handler(event,context=None)