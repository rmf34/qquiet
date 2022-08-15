import boto3

session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key='',
)

s3 = session.resource('s3')

# NOTE: root is /code
# PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
s3.Bucket('qquiet-dev').download_file('test.txt', '/tmp/test.txt')
