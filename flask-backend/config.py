import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'secret'

# There are three different ways to store the data in the application.
# You can choose 'datastore', 'cloudsql', or 'mongodb'. Be sure to
# configure the respective settings for the one you choose below.
# You do not have to configure the other data backends. If unsure, choose
# 'datastore' as it does not require any additional configuration.
DATA_BACKEND = 'mongodb'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'hackny-254317'
# PROJECT_ID = 'relieveu'
# Mongo configuration

MONGO_URI = \
    'mongodb+srv://wpflueger:2v9tWn8dazV2XflP@cluster0-ovrrv.gcp.mongodb.net/test?retryWrites=true&w=majority'
