import boto3

photo = PICTURE_NAME
image_bucket = BUCKET_NAME

rekognition_client = boto3.client('rekognition', aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key,
                                  aws_session_token=aws_session_token,
                                  region_name='us-east-1')

detect_facial_attributes = rekognition_client.detect_faces(
    Image={
        'S3Object': {
            'Bucket': image_bucket,
            'Name': photo
        }
    },
    Attributes=[
        'ALL'
    ]
)

print(detect_facial_attributes)
