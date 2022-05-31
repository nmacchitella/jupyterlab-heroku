# https://devcenter.heroku.com/articles/ssl-endpoint
#
import os
SECRET_KEY = os.environ.get('PASSWORD', False)

# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password="argon2:$argon2id$v=19$m=10240,t=10,p=8$ShJ/e/jKfyxoIGq8IOtEAw$P5os6s8T5TlqsvHvPBQK4czCeRujwJw19x1/hyfyIiQ"
print(SECRET_KEY)
#c.NotebookApp.token=""
