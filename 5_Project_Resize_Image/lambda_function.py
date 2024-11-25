import boto3
import io
from PIL import Image # pip install pillow
client = boto3.client('s3')

# bucket = event["Records"][0]['s3']['bucket']['name']
# key = event["Records"][0]['s3']['object']['key']
bucket = 'rawimagedata-i1234a'
key = 'images/lambda1.png'
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
destination_bucket = 'processimagedata-i1234a'
destination_key = key

client.put_object(
    Bucket=destination_bucket,
    Key=destination_key,
    Body=byte_value
)
output_buffer.close()
print("Resize Image Successfully")










