# https://devcenter.heroku.com/articles/ssl-endpoint
#
# As long as the notebook lives in the herokuapp.com domain,
# we have SSL certificates enabled for encryption purposes.
c.NotebookApp.ip = "*"
c.NotebookApp.open_browser = False
c.NotebookApp.password="sha1:bca9422a4bbf:6b2c319684b3b95d30245b6b3b9ee307245032bb"
c.NotebookApp.token=""
