
# This file is your default settings.. you may overide any settings for development and production

##################################################### FLASK SETTINGS #####################################################################
# Specifies that JSON should be rendered in UTF-8 rather than ASCI
JSON_AS_ASCII = False

#Specifies whether JSON should be sorted or not, sorted is useful for caching 
JSON_SORT_KEYS = False


#The amount of time static files should be cached
SEND_FILE_MAX_AGE_DEFAULT = 0

#The maximum ammount that is allowed to be uploaded in bytes 
MAX_CONTENT_LENGTH = 16*1024*1024

#The allowed extensions of file uploads
ALLOWED_EXTENSIONS = ['zip', 'csv']

