# Tencent COS

from dotenv import load_dotenv
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from utils import get_current_timestamp
import requests
import os


load_dotenv()

region = os.getenv('COS_REGION')
bucket = os.getenv('COS_BUCKET')
secret_id = os.getenv('COS_SECRET_ID')
secret_key = os.getenv('COS_SECRET_KEY')
save_path = os.getenv('COS_SAVE_PATH')

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=None, Scheme='https')
client = CosS3Client(config)


def cos_upload_img(img_old_url):
    try:
        stream = requests.get(img_old_url)
        new_img_name = f'{get_current_timestamp()}.png'
        resp = client.put_object(
            Bucket=bucket,
            Body=stream,
            Key=new_img_name,
        )
        if resp['ETag']:
            return f'https://{bucket}.cos.{region}.myqcloud.com/{new_img_name}'
        else:
            return ''
    except Exception as e:
        print(e)
