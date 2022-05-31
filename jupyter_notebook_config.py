# https://devcenter.heroku.com/articles/ssl-endpoint
#
SECRET_KEY = os.environ.get('PASSWORD', False)

# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password=SECRET_KEY 
c.NotebookApp.token=""
