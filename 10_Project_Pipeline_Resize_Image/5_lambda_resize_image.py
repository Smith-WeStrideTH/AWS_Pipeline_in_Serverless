import boto3
import io
from PIL import Image # pip install pillow
client = boto3.client('s3')

def lambda_handler(event,context):
    bucket = event["Records"][0]['s3']['bucket']['name']
    key = event["Records"][0]['s3']['object']['key']
    response = client.get_object(Bucket=bucket, Key=key)
    # read image
    image_data = response['Body'].read()
    image = Image.open(io.BytesIO(image_data))
    
    # process image
    new_width = 100
    new_height = 100
    resize_image = image.resize((new_width,new_height))
    resize_image = resize_image.convert('RGB')
    output_buffer = io.BytesIO()
    resize_image.save(output_buffer, format="JPEG")
    byte_value = output_buffer.getvalue()
    
    # write image to destination bucket
    destination_bucket = 'imagedatas3-destination-id1234a'
    destination_key = "process/"+ key
    
    client.put_object(
        Bucket=destination_bucket,
        Key=destination_key,
        Body=byte_value
    )
    output_buffer.close()
    print("Resize Image Successfully")
    return {
        'bucket': destination_bucket,
        'key': destination_key
    }











