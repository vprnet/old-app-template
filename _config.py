# Frozen Flask
FREEZER_DEFAULT_MIMETYPE = 'text/html'
FREEZER_IGNORE_MIMETYPE_WARNINGS = True

# Amazon S3 Settings
AWS_KEY = ''
AWS_SECRET_KEY = ''
AWS_BUCKET = ''
AWS_DIRECTORY = ''  # Use if S3 bucket is not root

# Cache Settings (units in seconds)
STATIC_EXPIRES = 60 * 24 * 3600
HTML_EXPIRES = 3600

# Upload Settings (ignores anything included below)
IGNORE_DIRECTORIES = ['.git', 'venv', 'sass', 'templates']
IGNORE_FILES = ['.DS_Store']
IGNORE_FILE_TYPES = ['.gz', '.pyc', '.py', '.rb', '.md']

if AWS_DIRECTORY:
    BASE_URL = 'http://' + AWS_BUCKET + '/' + AWS_DIRECTORY
    FREEZER_BASE_URL = BASE_URL
else:
    BASE_URL = 'http://' + AWS_BUCKET
