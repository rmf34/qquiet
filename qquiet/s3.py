import boto3

DEV_BUCKET = 'qquiet-dev'
class S3Storage():

    def session(self):
        return boto3.Session(
            aws_access_key_id='',
            aws_secret_access_key='',
        )

    def s3(self):
        return self.session().resource('s3').Bucket(DEV_BUCKET)

    def download(self, filename):
        # NOTE: root is /code
        # PROJECT_PATH = os.path.abspath(os.path.dirname(__name__))
        self.s3().download_file(f'audio/{filename}', f'/tmp/{filename}')

    def upload(self, temp_location, filename):
        self.s3().upload_file(temp_location, f'audio/{filename}') # from temp location

    def put(self, data, upload_file_path):
        self.s3().put_object(Bucket=DEV_BUCKET, Body=data, Key=upload_file_path)    # in memory

