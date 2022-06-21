import os

from s3contents import S3ContentsManager

try:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
except (NameError, KeyError):
    print('Using Bucketeer instead…')
    # Bucketeer addon.
    AWS_ACCESS_KEY_ID = os.environ['BUCKETEER_AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['BUCKETEER_AWS_SECRET_ACCESS_KEY']
    S3_BUCKET_NAME = os.environ['BUCKETEER_BUCKET_NAME']

PASSWORD = os.environ.get('PASSWORD', '')

c = get_config()
c.NotebookApp.contents_manager_class = S3ContentsManager
c.S3ContentsManager.access_key_id = AWS_ACCESS_KEY_ID
c.S3ContentsManager.secret_access_key = AWS_SECRET_ACCESS_KEY
c.S3ContentsManager.bucket = S3_BUCKET_NAME
c.S3ContentsManager.prefix = "beta/"
c.ServerApp.root_dir = ""

c.NotebookApp.token = ''
c.NotebookApp.password = 'argon2:$argon2id$v=19$m=10240,t=10,p=8$ubk10Rux17gywt5a3QT1DQ$g5eHBXyZmk7rQiNffl8LVOInEfgTq7Ttzrx9UrZquHE'

# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
